#!/usr/bin/python
# -*- coding: utf8 -*-
#IMPORT LIBRARY FOR MYSQL
import MySQLdb
#SETUP DATABASE INFORMATION
from DBconfig import DBHOST, DBUSER, DBPASSWORD, DBNAME

database = MySQLdb.connect(DBHOST, DBUSER, DBPASSWORD, DBNAME, charset="utf8", use_unicode=True)

cursor = database.cursor()

def create_hiragana():
    print("CREATING TABLE hiragana")
    cursor.execute("DROP TABLE IF EXISTS hiragana;")
    cursor.execute("""CREATE TABLE hiragana (
        start VARCHAR(2),
        a VARCHAR(2) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
        i VARCHAR(2) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
        u VARCHAR(2) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
        e VARCHAR(2) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
        o VARCHAR(2) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL);""")

    print("INSERTING DATA TO TABLE hiragana")
    cursor.execute("INSERT INTO hiragana (start, a, i, u, e, o) VALUES (%s, %s, %s, %s, %s, %s)", (u"a", u"あ", u"い", u"う", u"え", u"お"))
    cursor.execute("INSERT INTO hiragana (start, a, i, u, e, o) VALUES (%s, %s, %s, %s, %s, %s)", (u"k", u"か", u"き", u"く", u"け", u"こ"))
    cursor.execute("INSERT INTO hiragana (start, a, i, u, e, o) VALUES (%s, %s, %s, %s, %s, %s)", (u"s", u"さ", u"し", u"す", u"せ", u"そ"))
    cursor.execute("INSERT INTO hiragana (start, a, i, u, e, o) VALUES (%s, %s, %s, %s, %s, %s)", (u"t", u"た", u"ち", u"つ", u"て", u"と"))
    cursor.execute("INSERT INTO hiragana (start, a, i, u, e, o) VALUES (%s, %s, %s, %s, %s, %s)", (u"n", u"な", u"に", u"ぬ", u"ね", u"の"))
    cursor.execute("INSERT INTO hiragana (start, a, i, u, e, o) VALUES (%s, %s, %s, %s, %s, %s)", (u"h", u"は", u"ひ", u"ふ", u"へ", u"ほ"))
    cursor.execute("INSERT INTO hiragana (start, a, i, u, e, o) VALUES (%s, %s, %s, %s, %s, %s)", (u"m", u"ま", u"み", u"む", u"め", u"も"))
    cursor.execute("INSERT INTO hiragana (start, a, i, u, e, o) VALUES (%s, %s, %s, %s, %s, %s)", (u"r", u"ら", u"り", u"る", u"れ", u"ろ"))
    
    cursor.execute("INSERT INTO hiragana (start, a, i, u, e, o) VALUES (%s, %s, %s, %s, %s, %s)", (u"g", u"が", u"ぎ", u"ぐ", u"げ", u"ご"))
    cursor.execute("INSERT INTO hiragana (start, a, i, u, e, o) VALUES (%s, %s, %s, %s, %s, %s)", (u"z", u"ざ", u"じ", u"ず", u"ぜ", u"ぞ"))
    cursor.execute("INSERT INTO hiragana (start, a, i, u, e, o) VALUES (%s, %s, %s, %s, %s, %s)", (u"d", u"だ", u"ぢ", u"づ", u"で", u"ど"))
    cursor.execute("INSERT INTO hiragana (start, a, i, u, e, o) VALUES (%s, %s, %s, %s, %s, %s)", (u"b", u"ば", u"び", u"ぶ", u"べ", u"ぼ"))
    cursor.execute("INSERT INTO hiragana (start, a, i, u, e, o) VALUES (%s, %s, %s, %s, %s, %s)", (u"p", u"ぱ", u"ぴ", u"ぷ", u"ぺ", u"ぽ"))

    print("INSERTED DATA TO TABLE hiragana\n")
    database.commit()

def create_verb_specialform():
    print("CREATING TABLE verb_special_form")
    cursor.execute("DROP TABLE IF EXISTS verb_special_form")
    cursor.execute("""CREATE TABLE verb_special_form (
            dictionary_form VARCHAR(15) CHARACTER SET utf8 COLLATE utf8_general_ci,
            stem_form VARCHAR(15) CHARACTER SET utf8 COLLATE utf8_general_ci,
            present VARCHAR(15) CHARACTER SET utf8 COLLATE utf8_general_ci,
            negative VARCHAR(15) CHARACTER SET utf8 COLLATE utf8_general_ci,
            te_form VARCHAR(15) CHARACTER SET utf8 COLLATE utf8_general_ci,
            past VARCHAR(15) CHARACTER SET utf8 COLLATE utf8_general_ci,
            past_negative VARCHAR(15) CHARACTER SET utf8 COLLATE utf8_general_ci,
            negative_short VARCHAR(15) CHARACTER SET utf8 COLLATE utf8_general_ci,
            past_short VARCHAR(15) CHARACTER SET utf8 COLLATE utf8_general_ci,
            past_negative_short VARCHAR(15) CHARACTER SET utf8 COLLATE utf8_general_ci);""")

    print("INSERTING DATA TO TABLE verb_special_form")
    cursor.execute("INSERT INTO verb_special_form (dictionary_form, stem_form, present, negative, te_form, past, past_negative,negative_short, past_short, past_negative_short) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)", (u"くる", u"く", u"きます", u"きません", u"きて", u"きました", u"きませんでした",  u"こない", u"きた", u"こなかった"))
    cursor.execute("INSERT INTO verb_special_form (dictionary_form, stem_form, present, negative, te_form, past, past_negative,negative_short, past_short, past_negative_short) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)", (u"する", u"す", u"します", u"しません", u"して", u"しました", u"しませんでした",  u"しない", u"した", u"しなかった"))
    cursor.execute("INSERT INTO verb_special_form (dictionary_form, stem_form, present, negative, te_form, past, past_negative,negative_short, past_short, past_negative_short) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)", (u"いく", u"い", u"いきます", u"いきません", u"いって", u"いきました", u"いきませんでした",  u"いかない", u"いった", u"いかなかった"))

    print("INSERTED DATA TO TABLE verb_special_form\n")
    database.commit()

def create_adjective_specialform():
    print("CREATING TABLE adjective_special_form")
    cursor.execute("DROP TABLE IF EXISTS adjective_special_form")
    cursor.execute("""CREATE TABLE adjective_special_form (
            dictionary_form VARCHAR(15) CHARACTER SET utf8 COLLATE utf8_general_ci,
            present VARCHAR(15) CHARACTER SET utf8 COLLATE utf8_general_ci,
            negative VARCHAR(15) CHARACTER SET utf8 COLLATE utf8_general_ci,
            past VARCHAR(15) CHARACTER SET utf8 COLLATE utf8_general_ci,
            past_negative VARCHAR(15) CHARACTER SET utf8 COLLATE utf8_general_ci,
            te_form VARCHAR(15) CHARACTER SET utf8 COLLATE utf8_general_ci,
            negative_short VARCHAR(15) CHARACTER SET utf8 COLLATE utf8_general_ci,
            past_short VARCHAR(15) CHARACTER SET utf8 COLLATE utf8_general_ci,
            past_negative_short VARCHAR(15) CHARACTER SET utf8 COLLATE utf8_general_ci)""")
    
    print("INSERTING DATA TO TABLE adjective_special_form")
    cursor.execute("INSERT INTO adjective_special_form (dictionary_form, present, negative, past, past_negative, te_form, negative_short, past_short, past_negative_short) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)", (u"いい", u"いいです", u"よくないです", u"よかったです", u"よくなかったです", u"よくて", u"よくない", u"よかった", u"よくなかった"))
    
def create_ruverb():
    print("CREATING TABLE ru_verb")
    cursor.execute("DROP TABLE IF EXISTS ru_verb")
    cursor.execute("""CREATE TABLE ru_verb (
            verb VARCHAR(10) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL);""")

    print("INSERTING DATA TO TABLE ru_verb")
    cursor.execute("INSERT INTO ru_verb (verb) VALUES (%s)", (u"食べる",))
    cursor.execute("INSERT INTO ru_verb (verb) VALUES (%s)", (u"たべる",))
    cursor.execute("INSERT INTO ru_verb (verb) VALUES (%s)", (u"起きる",))
    cursor.execute("INSERT INTO ru_verb (verb) VALUES (%s)", (u"おきる",))
    cursor.execute("INSERT INTO ru_verb (verb) VALUES (%s)", (u"寝る",))
    cursor.execute("INSERT INTO ru_verb (verb) VALUES (%s)", (u"ねる",))
    cursor.execute("INSERT INTO ru_verb (verb) VALUES (%s)", (u"みる",))
    cursor.execute("INSERT INTO ru_verb (verb) VALUES (%s)", (u"見る",))
    cursor.execute("INSERT INTO ru_verb (verb) VALUES (%s)", (u"いる",))
    cursor.execute("INSERT INTO ru_verb (verb) VALUES (%s)", (u"出かける",))
    cursor.execute("INSERT INTO ru_verb (verb) VALUES (%s)", (u"でかける",))
    cursor.execute("INSERT INTO ru_verb (verb) VALUES (%s)", (u"開ける",))
    cursor.execute("INSERT INTO ru_verb (verb) VALUES (%s)", (u"あける",))
    cursor.execute("INSERT INTO ru_verb (verb) VALUES (%s)", (u"教える",))
    cursor.execute("INSERT INTO ru_verb (verb) VALUES (%s)", (u"おしえる",))
    cursor.execute("INSERT INTO ru_verb (verb) VALUES (%s)", (u"降りる",))
    cursor.execute("INSERT INTO ru_verb (verb) VALUES (%s)", (u"おりる",))
    cursor.execute("INSERT INTO ru_verb (verb) VALUES (%s)", (u"閉める",))
    cursor.execute("INSERT INTO ru_verb (verb) VALUES (%s)", (u"しめる",))
    cursor.execute("INSERT INTO ru_verb (verb) VALUES (%s)", (u"シャワーを浴びる",))
    cursor.execute("INSERT INTO ru_verb (verb) VALUES (%s)", (u"シャワーをあびる",))
    cursor.execute("INSERT INTO ru_verb (verb) VALUES (%s)", (u"電話をかける",))
    cursor.execute("INSERT INTO ru_verb (verb) VALUES (%s)", (u"でんわをかける",))
    cursor.execute("INSERT INTO ru_verb (verb) VALUES (%s)", (u"忘れる",))
    cursor.execute("INSERT INTO ru_verb (verb) VALUES (%s)", (u"わすれる",))
    cursor.execute("INSERT INTO ru_verb (verb) VALUES (%s)", (u"かける",))
    cursor.execute("INSERT INTO ru_verb (verb) VALUES (%s)", (u"きる",))
    cursor.execute("INSERT INTO ru_verb (verb) VALUES (%s)", (u"つとめる",))
    cursor.execute("INSERT INTO ru_verb (verb) VALUES (%s)", (u"やせる",))
    cursor.execute("INSERT INTO ru_verb (verb) VALUES (%s)", (u"じろじろみる",))
    cursor.execute("INSERT INTO ru_verb (verb) VALUES (%s)", (u"すてる",))
    cursor.execute("INSERT INTO ru_verb (verb) VALUES (%s)", (u"はじめる",))
    cursor.execute("INSERT INTO ru_verb (verb) VALUES (%s)", (u"おぼえる",))
    cursor.execute("INSERT INTO ru_verb (verb) VALUES (%s)", (u"でる",))
    cursor.execute("INSERT INTO ru_verb (verb) VALUES (%s)", (u"出る",))

    print("INSERTED DATA TO TABLE ru_verb\n")
    database.commit()

def create_verb():
    print("CREATING TABLE verb")
    cursor.execute("DROP TABLE IF EXISTS verb;")
    cursor.execute("""CREATE TABLE verb(
        word VARCHAR(15) CHARACTER SET utf8 COLLATE utf8_general_ci,
        meaning VARCHAR(50),
        chapter INT);""")
    
    print("INSERTING DATA TO TABLE verb")
    cursor.execute("INSERT INTO verb (word, meaning, chapter) VALUES (%s, %s, 3)", (u"いく", u"to go"))
    cursor.execute("INSERT INTO verb (word, meaning, chapter) VALUES (%s, %s, 3)", (u"かえる", u"to return"))
    cursor.execute("INSERT INTO verb (word, meaning, chapter) VALUES (%s, %s, 3)", (u"きく", u"to listen"))
    cursor.execute("INSERT INTO verb (word, meaning, chapter) VALUES (%s, %s, 3)", (u"のむ", u"to drink"))
    cursor.execute("INSERT INTO verb (word, meaning, chapter) VALUES (%s, %s, 3)", (u"はなす", u"to speak"))
    cursor.execute("INSERT INTO verb (word, meaning, chapter) VALUES (%s, %s, 3)", (u"よむ", u"to read"))
    cursor.execute("INSERT INTO verb (word, meaning, chapter) VALUES (%s, %s, 3)", (u"おきる", u"to get up"))
    cursor.execute("INSERT INTO verb (word, meaning, chapter) VALUES (%s, %s, 3)", (u"たべる", u"to eat"))
    cursor.execute("INSERT INTO verb (word, meaning, chapter) VALUES (%s, %s, 3)", (u"ねる", u"to sleep"))
    cursor.execute("INSERT INTO verb (word, meaning, chapter) VALUES (%s, %s, 3)", (u"みる", u"to see"))
    cursor.execute("INSERT INTO verb (word, meaning, chapter) VALUES (%s, %s, 4)", (u"あう", u"to meet"))
    cursor.execute("INSERT INTO verb (word, meaning, chapter) VALUES (%s, %s, 4)", (u"ある", u"there is"))
    cursor.execute("INSERT INTO verb (word, meaning, chapter) VALUES (%s, %s, 4)", (u"かう", u"to buy"))
    cursor.execute("INSERT INTO verb (word, meaning, chapter) VALUES (%s, %s, 4)", (u"かく", u"to write"))
    cursor.execute("INSERT INTO verb (word, meaning, chapter) VALUES (%s, %s, 4)", (u"とる", u"to take (a picture)"))
    cursor.execute("INSERT INTO verb (word, meaning, chapter) VALUES (%s, %s, 4)", (u"まつ", u"to wait"))
    cursor.execute("INSERT INTO verb (word, meaning, chapter) VALUES (%s, %s, 4)", (u"わかる", u"to understand"))
    cursor.execute("INSERT INTO verb (word, meaning, chapter) VALUES (%s, %s, 4)", (u"いる", u"(a person) is in"))
    cursor.execute("INSERT INTO verb (word, meaning, chapter) VALUES (%s, %s, 5)", (u"およぐ", u"to swim"))
    cursor.execute("INSERT INTO verb (word, meaning, chapter) VALUES (%s, %s, 5)", (u"きく", u"to ask"))
    cursor.execute("INSERT INTO verb (word, meaning, chapter) VALUES (%s, %s, 5)", (u"のる", u"to ride"))
    cursor.execute("INSERT INTO verb (word, meaning, chapter) VALUES (%s, %s, 5)", (u"やる", u"to do"))
    cursor.execute("INSERT INTO verb (word, meaning, chapter) VALUES (%s, %s, 5)", (u"でかける", u"to go out"))
    cursor.execute("INSERT INTO verb (word, meaning, chapter) VALUES (%s, %s, 6)", (u"あける", u"to open"))
    cursor.execute("INSERT INTO verb (word, meaning, chapter) VALUES (%s, %s, 6)", (u"おしえる", u"to teach"))
    cursor.execute("INSERT INTO verb (word, meaning, chapter) VALUES (%s, %s, 6)", (u"おりる", u"to get off"))
    cursor.execute("INSERT INTO verb (word, meaning, chapter) VALUES (%s, %s, 6)", (u"かりる", u"to borrow"))
    cursor.execute("INSERT INTO verb (word, meaning, chapter) VALUES (%s, %s, 6)", (u"しめる", u"to close"))
    cursor.execute("INSERT INTO verb (word, meaning, chapter) VALUES (%s, %s, 6)", (u"シャワーをあびる", u"to take a shower"))
    cursor.execute("INSERT INTO verb (word, meaning, chapter) VALUES (%s, %s, 6)", (u"つける", u"to turn on"))
    cursor.execute("INSERT INTO verb (word, meaning, chapter) VALUES (%s, %s, 6)", (u"でんわをかける", u"to make a phone call"))
    cursor.execute("INSERT INTO verb (word, meaning, chapter) VALUES (%s, %s, 6)", (u"わすれる", u"to forget"))
    cursor.execute("INSERT INTO verb (word, meaning, chapter) VALUES (%s, %s, 7)", (u"うたう", u"to sing"))
    cursor.execute("INSERT INTO verb (word, meaning, chapter) VALUES (%s, %s, 7)", (u"かぶる", u"to put on (hat)"))
    cursor.execute("INSERT INTO verb (word, meaning, chapter) VALUES (%s, %s, 7)", (u"しる", u"to get to know"))
    cursor.execute("INSERT INTO verb (word, meaning, chapter) VALUES (%s, %s, 7)", (u"すむ", u"to live"))
    cursor.execute("INSERT INTO verb (word, meaning, chapter) VALUES (%s, %s, 7)", (u"はく", u"to put on (item below your waist)"))
    cursor.execute("INSERT INTO verb (word, meaning, chapter) VALUES (%s, %s, 7)", (u"ふとる", u"to gain weight"))
    cursor.execute("INSERT INTO verb (word, meaning, chapter) VALUES (%s, %s, 7)", (u"かける", u"to put on (glasses)"))
    cursor.execute("INSERT INTO verb (word, meaning, chapter) VALUES (%s, %s, 7)", (u"きる", u"to put on (clothes above your waist)"))
    cursor.execute("INSERT INTO verb (word, meaning, chapter) VALUES (%s, %s, 7)", (u"つとめる", u"to work for"))
    cursor.execute("INSERT INTO verb (word, meaning, chapter) VALUES (%s, %s, 7)", (u"やせる", u"to be thin"))
    cursor.execute("INSERT INTO verb (word, meaning, chapter) VALUES (%s, %s, 8)", (u"じろじろみる", u"to stare"))
    cursor.execute("INSERT INTO verb (word, meaning, chapter) VALUES (%s, %s, 8)", (u"すてる", u"to throw away"))
    cursor.execute("INSERT INTO verb (word, meaning, chapter) VALUES (%s, %s, 8)", (u"はじめる", u"to begin"))

    cursor.execute("INSERT INTO verb (word, meaning, chapter) VALUES (%s, %s, 9)", (u"おどる", u"to dance"))
    cursor.execute("INSERT INTO verb (word, meaning, chapter) VALUES (%s, %s, 9)", (u"おわる", u"(something) ends"))
    cursor.execute("INSERT INTO verb (word, meaning, chapter) VALUES (%s, %s, 9)", (u"にんきがある", u"to be popular"))
    cursor.execute("INSERT INTO verb (word, meaning, chapter) VALUES (%s, %s, 9)", (u"はじまる", u"(something) begins"))
    cursor.execute("INSERT INTO verb (word, meaning, chapter) VALUES (%s, %s, 9)", (u"ひく", u"to play (string instrument or piano)"))
    cursor.execute("INSERT INTO verb (word, meaning, chapter) VALUES (%s, %s, 9)", (u"もらう", u"to get (from somebody)"))
    cursor.execute("INSERT INTO verb (word, meaning, chapter) VALUES (%s, %s, 9)", (u"おぼえる", u"to memorize"))
    cursor.execute("INSERT INTO verb (word, meaning, chapter) VALUES (%s, %s, 9)", (u"でる", u"to exit/ to appear"))
    
    print("INSERTED DATA TO TABLE verb")
    database.commit()
 
def create_vocab():
    print("CREATING TABLE vocab")
    cursor.execute("DROP TABLE IF EXISTS vocab;")
    cursor.execute("""CREATE TABLE vocab(
            word VARCHAR(30) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
            meaning VARCHAR(50),
            chapter INT
            );""")

    print("INSERTING DATA TO TABLE vocab")
    cursor.execute("INSERT INTO vocab (word, meaning, chapter) VALUES (%s, %s, 1)", (u"いま", u"now"))
    cursor.execute("INSERT INTO vocab (word, meaning, chapter) VALUES (%s, %s, 1)", (u"えいご", u"English"))
    cursor.execute("INSERT INTO vocab (word, meaning, chapter) VALUES (%s, %s, 1)", (u"がくせえ", u"student"))
    cursor.execute("INSERT INTO vocab (word, meaning, chapter) VALUES (%s, %s, 1)", (u"こうこう", u"high school"))
    cursor.execute("INSERT INTO vocab (word, meaning, chapter) VALUES (%s, %s, 1)", (u"ごご", u"P.M."))
    cursor.execute("INSERT INTO vocab (word, meaning, chapter) VALUES (%s, %s, 1)", (u"ごぜん", u"A.M."))
    cursor.execute("INSERT INTO vocab (word, meaning, chapter) VALUES (%s, %s, 1)", (u"さい", u"...years old"))
    cursor.execute("INSERT INTO vocab (word, meaning, chapter) VALUES (%s, %s, 1)", (u"せんこう", u"major"))
    cursor.execute("INSERT INTO vocab (word, meaning, chapter) VALUES (%s, %s, 1)", (u"せんせえ", u"teacher"))
    cursor.execute("INSERT INTO vocab (word, meaning, chapter) VALUES (%s, %s, 1)", (u"だいがく", u"university"))
    cursor.execute("INSERT INTO vocab (word, meaning, chapter) VALUES (%s, %s, 1)", (u"でんわい", u"telephone"))
    cursor.execute("INSERT INTO vocab (word, meaning, chapter) VALUES (%s, %s, 1)", (u"ともだち", u"friend"))
    cursor.execute("INSERT INTO vocab (word, meaning, chapter) VALUES (%s, %s, 1)", (u"なまえ", u"name"))
    cursor.execute("INSERT INTO vocab (word, meaning, chapter) VALUES (%s, %s, 1)", (u"なに", u"what"))
    cursor.execute("INSERT INTO vocab (word, meaning, chapter) VALUES (%s, %s, 1)", (u"にほん", u"Japan"))
    cursor.execute("INSERT INTO vocab (word, meaning, chapter) VALUES (%s, %s, 1)", (u"はん", u"half"))
    cursor.execute("INSERT INTO vocab (word, meaning, chapter) VALUES (%s, %s, 1)", (u"ばんごう", u"number"))
    cursor.execute("INSERT INTO vocab (word, meaning, chapter) VALUES (%s, %s, 1)", (u"リュがくせえ", u"international student"))
    cursor.execute("INSERT INTO vocab (word, meaning, chapter) VALUES (%s, %s, 1)", (u"わたし", u"I"))
    cursor.execute("INSERT INTO vocab (word, meaning, chapter) VALUES (%s, %s, 1)", (u"かがく", u"science"))
    cursor.execute("INSERT INTO vocab (word, meaning, chapter) VALUES (%s, %s, 1)", (u"けえざい", u"economics"))
    cursor.execute("INSERT INTO vocab (word, meaning, chapter) VALUES (%s, %s, 1)", (u"こくさいかんけえ", u"international relations"))
    cursor.execute("INSERT INTO vocab (word, meaning, chapter) VALUES (%s, %s, 1)", (u"じんるいがく", u"anthropology"))
    cursor.execute("INSERT INTO vocab (word, meaning, chapter) VALUES (%s, %s, 1)", (u"せえじ", u"politics"))
    cursor.execute("INSERT INTO vocab (word, meaning, chapter) VALUES (%s, %s, 1)", (u"ぶんがく", u"literature"))
    cursor.execute("INSERT INTO vocab (word, meaning, chapter) VALUES (%s, %s, 1)", (u"れきし", u"history"))
    cursor.execute("INSERT INTO vocab (word, meaning, chapter) VALUES (%s, %s, 1)", (u"しごと", u"job"))
    cursor.execute("INSERT INTO vocab (word, meaning, chapter) VALUES (%s, %s, 1)", (u"いしゃ", u"doctor"))
    cursor.execute("INSERT INTO vocab (word, meaning, chapter) VALUES (%s, %s, 1)", (u"かいしゃいん", u"office worker"))
    cursor.execute("INSERT INTO vocab (word, meaning, chapter) VALUES (%s, %s, 1)", (u"こうこうせい", u"high school student"))
    cursor.execute("INSERT INTO vocab (word, meaning, chapter) VALUES (%s, %s, 1)", (u"しゅふ", u"housewife"))
    cursor.execute("INSERT INTO vocab (word, meaning, chapter) VALUES (%s, %s, 1)", (u"だいがくいんせえ", u"graduate student"))
    cursor.execute("INSERT INTO vocab (word, meaning, chapter) VALUES (%s, %s, 1)", (u"だいがくせえ", u"college student"))
    cursor.execute("INSERT INTO vocab (word, meaning, chapter) VALUES (%s, %s, 1)", (u"べんごし", u"lawyer"))
    cursor.execute("INSERT INTO vocab (word, meaning, chapter) VALUES (%s, %s, 1)", (u"おかあさん", u"mother"))
    cursor.execute("INSERT INTO vocab (word, meaning, chapter) VALUES (%s, %s, 1)", (u"おとうさん", u"father"))
    cursor.execute("INSERT INTO vocab (word, meaning, chapter) VALUES (%s, %s, 1)", (u"おねえさん", u"older sister"))
    cursor.execute("INSERT INTO vocab (word, meaning, chapter) VALUES (%s, %s, 1)", (u"おにいさん", u"older brother"))
    cursor.execute("INSERT INTO vocab (word, meaning, chapter) VALUES (%s, %s, 1)", (u"いもうと", u"younger sister"))
    cursor.execute("INSERT INTO vocab (word, meaning, chapter) VALUES (%s, %s, 1)", (u"おとうと", u"younger brother"))
    
    cursor.execute("INSERT INTO vocab (word, meaning, chapter) VALUES (%s, %s, 9)", (u"いいこ", u"good child"))
    cursor.execute("INSERT INTO vocab (word, meaning, chapter) VALUES (%s, %s, 9)", (u"いろ", u"color"))
    cursor.execute("INSERT INTO vocab (word, meaning, chapter) VALUES (%s, %s, 9)", (u"おべんとう", u"boxed lunch"))
    cursor.execute("INSERT INTO vocab (word, meaning, chapter) VALUES (%s, %s, 9)", (u"かぶき", u"trad. Japanese theatrical art"))
    cursor.execute("INSERT INTO vocab (word, meaning, chapter) VALUES (%s, %s, 9)", (u"きょねん", u"last year"))
    cursor.execute("INSERT INTO vocab (word, meaning, chapter) VALUES (%s, %s, 9)", (u"くすり", u"medicine"))
    cursor.execute("INSERT INTO vocab (word, meaning, chapter) VALUES (%s, %s, 9)", (u"こんど", u"near future"))
    cursor.execute("INSERT INTO vocab (word, meaning, chapter) VALUES (%s, %s, 9)", (u"さくぶん", u"essay"))
    cursor.execute("INSERT INTO vocab (word, meaning, chapter) VALUES (%s, %s, 9)", (u"しけん", u"exam"))
    cursor.execute("INSERT INTO vocab (word, meaning, chapter) VALUES (%s, %s, 9)", (u"せんげつ", u"last month"))
    cursor.execute("INSERT INTO vocab (word, meaning, chapter) VALUES (%s, %s, 9)", (u"たんご", u"word/vocabulary"))
    cursor.execute("INSERT INTO vocab (word, meaning, chapter) VALUES (%s, %s, 9)", (u"びょうき", u"illness"))
    cursor.execute("INSERT INTO vocab (word, meaning, chapter) VALUES (%s, %s, 9)", (u"から", u"from......"))
    cursor.execute("INSERT INTO vocab (word, meaning, chapter) VALUES (%s, %s, 9)", (u"ぜひ", u"by all mean"))
    cursor.execute("INSERT INTO vocab (word, meaning, chapter) VALUES (%s, %s, 9)", (u"よころで", u"by the way"))
    cursor.execute("INSERT INTO vocab (word, meaning, chapter) VALUES (%s, %s, 9)", (u"みんな", u"all"))
    cursor.execute("INSERT INTO vocab (word, meaning, chapter) VALUES (%s, %s, 9)", (u"もう", u"already"))
    
    print("INSERTED DATA TO TABLE vocab")
    database.commit()



#create_hiragana()
#create_verb_specialform()
create_adjective_specialform()
#create_ruverb()
#create_verb()
#create_vocab()
