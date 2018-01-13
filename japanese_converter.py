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
        "/question/{year}/{type}":"use random to get random year or type, only /first_year/verb is implemented for now"}

all_years = ["first_year"]
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
        elif path[0] == "question":
            return getQuestion(path[1], path[2], self.dbHandler)
        else:
            return convertJson(instruction)

    def disconnect(self):
        self.dbHandler.disconnect()


#GET A RANDOM QUESTION
def getQuestion(year, q_type, database):
    output = {}

    selectedYear = year
    if year == "random":
        selectedYear = random.choice(all_years)
    
    if selectedYear in all_years:
        if q_type == "verb":
            #getting all verbs from the corresponding year
            query = "SELECT * FROM " + year + "_verb"
            info = database.getOutput(query)
            
            question = random.choice(info)
            output["verb"] = question["word"]
            output["meaning"] = question["meaning"]
            conjugation = verbConversion(output["verb"], database)
            #select what form to ask
            if selectedYear == "first_year":
                output["question"] = random.choice(first_year)
                output["answer"] = conjugation[output["question"]]
            elif selectedYear == "second_year":
                verb_form = first_year + second_year
                output["question"] = random.choice(verb_form)
                output["answer"] = conjugation[output["question"]]
                
        else:
            output['error'] = "not implemented yet"
    else:
        output['error'] = "invalid year"
    return convertJson(output)

#CONVERTING VERB INTO DIFFERENT FORM
def verbConversion(verb, database):
    #creating dictionary for output
    data = {}
    data['dictionary_form'] = verb
    print "checking verb : " + verb

    #check if it is special form
    info = database.getOutput("SELECT * FROM special_form")

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
    print verb
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
        if data['te_form'][-1] == "て":
            data['past_short'] = data['te_form'][:-1] + u"た"
        else :
            data['past_short'] = data['te_form'][:-1] + u"だ"
        data['past_negative_short'] = data['negative_short'][:-2] + u"なかった"
    else:
        data['error'] = "not working"
    return data



