# -*- coding: utf-8 -*-
#IMPORT CLASS TO CONNECT MYSQL
import database_connect
#IMPORT JSON TO PARSE THE DATA
import json
#IMPORT RANDOM TO GENERATE QUESTIONS
import random

#CONSTANT ARRAY
instruction = {"instruction":"use the following path to get more result",
        "/verbConvert/{verb}":"this will show you most verb conjugation",
        "/question/verb/{year/chapter}/{range}":"use random to get random year or type, example /question/verb/year/1",
        "/question/vocab/{year/chapter}/{range}/{type}":"type refers to mc or short question"}

first_year = ["present", "negative", "te_form", "past", "past_negative", "negative_short"]
second_year = ["past_negative_short", "past_short"]

def convertJson(inputArray):
    return json.dumps(inputArray)

class JapConverter:
    dbHandler = None
    
    def init(self):
        self.dbHandler = database_connect.DatabaseHandler()

    def getResult(self, path):
        if path[0] == "verbConvert":
            return convertJson(verbConversion(path[1], self.dbHandler))
        elif path[0] == "adjectiveConvert":
            return convertJson(adjectiveConversion(path[1], self.dbHandler))
        elif path[0] == "question":
            return convertJson(getQuestion(path[1:], self.dbHandler))
        else:
            return convertJson(instruction)

    def disconnect(self):
        self.dbHandler.disconnect()


#GET A RANDOM QUESTION
def getQuestion(question_type, database):
    if question_type[0] == "verb":
        return getVerbQuestion(question_type[1], int(question_type[2]), database)
    elif question_type[0] == "adjective":
        return getAdjectiveQuestion(question_type[1], int(question_type[2]), database)
    elif question_type[0] == "vocab":
        return getVocabQuestion(question_type[1], int(question_type[2]), question_type[3], database)
    else:
        return {"error" : "invalid type of question"}
            

def getVocabQuestion(selectWith, selectRange, question_type, database):
    output = {}
    query = None
    randNum = random.randint(0, 2)
    if randNum == 0 or (selectWith == "chapter" and selectRange < 3):
        query = "SELECT * FROM vocab " + getChapterQuery(selectWith, selectRange)
    elif randNum == 1:
        query = "SELECT * FROM verb " + getChapterQuery(selectWith, selectRange)
    else:
        query = "SELECT * FROM adjective " + getChapterQuery(selectWith, selectRange)

    #getting the information from the databse
    info = database.getOutput(query)
    if len(info) == 0:
        output["error"] = "nothing inside database"

    question = random.choice(info)
    #select what type of question
    if question_type == "short_q":
        output["meaning"] = question["meaning"]
        output["vocab"] = question["word"]
    elif question_type == "mc_meaning":
        output["question"] = question["word"]
        info.remove(question)
        choice = []
        choice.append(random.choice(info))
        choice.append(random.choice(info))
        choice.append(random.choice(info))
        answer_at = random.randint(0,3)
        for i in range(4):
            if i == answer_at:
                output[chr(97+i)] = question["meaning"]
            else:
                output[chr(97+i)] = choice.pop()["meaning"]
        output["answer"] = str(answer_at)
    elif question_type == "mc_word":
        output["question"] = question["meaning"]
        info.remove(question)
        choice = []
        choice.append(random.choice(info))
        choice.append(random.choice(info))
        choice.append(random.choice(info))
        answer_at = random.randint(0,3)
        for i in range(4):
            if i == answer_at:
                output[chr(97+i)] = question["word"]
            else:
                output[chr(97+i)] = choice.pop()["word"]
        output["answer"] = str(answer_at)
    else:
        output["error"] = "invalid question type"

    return output

def getAdjectiveQuestion(selectWith, selectRange, database):
    output = {}
    year = None
    query = "SELECT * FROM adjective " + getChapterQuery(selectWith, selectRange)
    if selectWith == "year":
        year = selectRange
    elif selectWith == "chapter":
        if selectRange <= 8:
            year = 1
        elif selectRange > 8:
            year = 2
        else:
            year = 0
    else:
        output["error"] = "invalid input"
        return output

    #getting the information from the database
    info = database.getOutput(query)
    if len(info) == 0:
        output["error"] = "nothing inside database"
        return output
    question = random.choice(info)
    output["adjective"] = question["word"]
    output["meaning"] = question["meaning"]
    conjugation = adjectiveConversion(output["adjective"], database)
    #select what form to ask
    if year == 1:
        output["question"] = random.choice(first_year)
        output["answer"] = conjugation[output["question"]]
    else:
        adjective_form = first_year + second_year
        output["question"] = random.choice(adjective_form)
        output["answer"] = conjugation[output["question"]]
        
    return output]


def getVerbQuestion(selectWith, selectRange, database):
    output = {}
    year = None

    query = "SELECT * FROM verb " + getChapterQuery(selectWith, selectRange)
    if selectWith == "year":
        year = selectRange
    elif selectWith == "chapter":
        if selectRange <= 8:
            year = 1
        elif selectRange > 8:
            year = 2
        else:
            year = 0
    else:
        output["error"] = "invalid input"
        return output

    #getting the information from the database
    info = database.getOutput(query)
    if len(info) == 0:
        output["error"] = "nothing inside database"
        return output
    question = random.choice(info)
    output["verb"] = question["word"]
    output["meaning"] = question["meaning"]
    conjugation = verbConversion(output["verb"], database)
    #select what form to ask
    if year == 1:
        output["question"] = random.choice(first_year)
        output["answer"] = conjugation[output["question"]]
    else:
        verb_form = first_year + second_year
        output["question"] = random.choice(verb_form)
        output["answer"] = conjugation[output["question"]]

    return output

#GET THE CHAPTER QUERY
def getChapterQuery(selectWith, selectRange):
    if selectWith == "year":
        if selectRange == 1:
            return "WHERE chapter <= 8"
        elif selectRange == 2:
            return "WHERE chapter > 8"
        else:
            return ""
    return "WHERE chapter = " + str(selectRange)

#CONVERTING ADJECTIVE INTO DIFFERENT FORMS
def adjectiveConversion(adjective, database):
    #creating dictionary for output
    data = {}
    data['dictionary_form'] = adjective

    #check if it is special form
    info = database.getOutput("SELECT * FROM adjective_special_form")

    for words in info:
        if adjective == words['dictionary_form']:
            return words

    #check if it is i or na adjective
    if adjective[-1] == u"い":
        help_form = adjective[:-1]
        data["present"] = adjective + u"です"
        data["negative"] = help_form + u"くないです"
        data["past"] = help_form + u"かったです"
        data["past_negative"] = help_form + u"くなかったです"
        data["te_form"] = help_form + u"くて"
        data["negative_short"] = help_form + u"くない"
        data["past_short"] = help_form + u"かった"
        data["past_negative_short"] = help_form + u"くなかった"
    elif adjective[-1] == u"な":
        help_form = adjective[:-1]
        data["present"] = help_form + u"です"
        data["negative"] = help_form + u"じゃないです"
        data["past"] = help_form + u"でした"
        data["past_negative"] = help_form + u"じゃなかったです"
        data["te_form"] = help_form + u"で"
        data["negative_short"] = help_form + u"じゃない"
        data["past_short"] = help_form + u"だった"
        data["past_negative_short"] = help_form + u"じゃなかった"
    else:
        data["error"] = "not an adjective"
    
    return data


#CONVERTING VERB INTO DIFFERENT FORMS
def verbConversion(verb, database):
    #creating dictionary for output
    data = {}
    data['dictionary_form'] = verb
    print "checking verb : " + verb

    #check if it is special form
    info = database.getOutput("SELECT * FROM verb_special_form")

    for words in info:
        if verb == words['dictionary_form']:
            return words

    #check if it is ru verb
    info = database.getOutputArray("SELECT * FROM ru_verb")
    if verb in info:
        data['stem_form'] = verb[:-1]
        data['present'] = verb[:-1] + u"ます"
        data['nagative'] = verb[:-1] + u"ません"
        data['past'] = verb[:-1] + u"ました"
        data['past_negative'] = verb[:-1] + u"ませんでした"
        data['te_form'] = verb[:-1] + u"て"
        data['negative_short'] = verb[:-1] + u"ない"
        data['past_short'] = verb[:-1] + u"た"
        data['past_negative_short'] = verb[:-1] + u"なかった"
        return data

    #getting hiragana to convert
    info = database.getOutput("SELECT * FROM hiragana")
    iletter = None
    aletter = None
    starting = None
    for row in info:
        if verb[-1] == row['u']:
            starting = row['start']
            iletter = row['i']
            if starting == 'a':
                aletter = u"わ"
            else:
                aletter = row['a']
            break

    if starting != None:
        stem = verb[:-1] + iletter
        data['stem_form'] = stem
        data['present'] = stem + u"ます"
        data['negative'] = stem + u"ません"
        data['past'] = stem + u"ました"
        data['past_negative'] = stem + u"ませんでした"
        #different conversion for te-form
        if starting == "a" or starting == "t" or starting == "r":
            data['te_form'] = verb[:-1] + u"って"
        elif starting == "m" or starting == "b" or starting == "n":
            data['te_form'] = verb[:-1] + u"んで"
        elif starting == "k":
            data['te_form'] = verb[:-1] + u"いて"
        elif starting == "g":
            data['te_form'] = verb[:-1] + u"いで"
        elif starting == "s":
            data['te_form'] = verb[:-1] + u"してi"
        #negative short
        data['negative_short'] = verb[:-1] + aletter + u"ない"
        if data['te_form'][-1] == u"て":
            data['past_short'] = data['te_form'][:-1] + u"た"
        else :
            data['past_short'] = data['te_form'][:-1] + u"だ"
        data['past_negative_short'] = data['negative_short'][:-2] + u"なかった"
    else:
        data['error'] = "not a verb"
    return data



