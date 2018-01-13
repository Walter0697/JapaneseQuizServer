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

def create_specialform():
    print("CREATING TABLE special_form")
    cursor.execute("DROP TABLE IF EXISTS special_form")
    cursor.execute("""CREATE TABLE special_form (
            dictionary_form VARCHAR(15) CHARACTER SET utf8 COLLATE utf8_general_ci,
            stem_form VARCHAR(15) CHARACTER SET utf8 COLLATE utf8_general_ci,
            present VARCHAR(15) CHARACTER SET utf8 COLLATE utf8_general_ci,
            negative VARCHAR(15) CHARACTER SET utf8 COLLATE utf8_general_ci,
            te_form VARCHAR(15) CHARACTER SET utf8 COLLATE utf8_general_ci,
            past VARCHAR(15) CHARACTER SET utf8 COLLATE utf8_general_ci,
            past_negative VARCHAR(15) CHARACTER SET utf8 COLLATE utf8_general_ci,
            negative_short VARCHAR(15) CHARACTER SET utf8 COLLATE utf8_general_ci,
            past_short VARCHAR(15) CHARACTER SET utf8 COLLATE utf8_general_ci,
            past_negative_short VARCHAR(15) CHARACTER SET utf8 COLLATE utf8_general_ci
            );""")

    print("INSERTING DATA TO TABLE special_form")
    cursor.execute("INSERT INTO special_form (dictionary_form, stem_form, present, negative, te_form, past, past_negative,negative_short, past_short, past_negative_short) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)", (u"くる", u"く", u"きます", u"きません", u"きて", u"きました", u"きませんでした",  u"こない", u"きた", u"こなかった"))
    cursor.execute("INSERT INTO special_form (dictionary_form, stem_form, present, negative, te_form, past, past_negative,negative_short, past_short, past_negative_short) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)", (u"する", u"す", u"します", u"しません", u"して", u"しました", u"しませんでした",  u"しない", u"した", u"しなかった"))
    cursor.execute("INSERT INTO special_form (dictionary_form, stem_form, present, negative, te_form, past, past_negative,negative_short, past_short, past_negative_short) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)", (u"いく", u"い", u"いきます", u"いきません", u"いって", u"いきました", u"いきませんでした",  u"いかない", u"いった", u"いかなかった"))

    print("INSERTED DATA TO TABLE special_form\n")
    database.commit()

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

    print("INSERTED DATA TO TABLE ru_verb\n")
    database.commit()

def create_verb():
    print("CREATING TABLE first_year_verb")
    cursor.execute("DROP TABLE IF EXISTS first_year_verb;")
    cursor.execute("""CREATE TABLE first_year_verb(
        word VARCHAR(15) CHARACTER SET utf8 COLLATE utf8_general_ci,
        meaning VARCHAR(50));""")
    
    print("INSERTING DATA TO TABLE first_year_verb")
    cursor.execute("INSERT INTO first_year_verb (word, meaning) VALUES (%s, %s)", (u"いく", u"to go"))
    cursor.execute("INSERT INTO first_year_verb (word, meaning) VALUES (%s, %s)", (u"かえる", u"to return"))
    cursor.execute("INSERT INTO first_year_verb (word, meaning) VALUES (%s, %s)", (u"きく", u"to listen"))
    cursor.execute("INSERT INTO first_year_verb (word, meaning) VALUES (%s, %s)", (u"のむ", u"to drink"))
    cursor.execute("INSERT INTO first_year_verb (word, meaning) VALUES (%s, %s)", (u"はなす", u"to speak"))
    cursor.execute("INSERT INTO first_year_verb (word, meaning) VALUES (%s, %s)", (u"よむ", u"to read"))
    cursor.execute("INSERT INTO first_year_verb (word, meaning) VALUES (%s, %s)", (u"おきる", u"to get up"))
    cursor.execute("INSERT INTO first_year_verb (word, meaning) VALUES (%s, %s)", (u"たべる", u"to eat"))
    cursor.execute("INSERT INTO first_year_verb (word, meaning) VALUES (%s, %s)", (u"ねる", u"to sleep"))
    cursor.execute("INSERT INTO first_year_verb (word, meaning) VALUES (%s, %s)", (u"みる", u"to see"))
    cursor.execute("INSERT INTO first_year_verb (word, meaning) VALUES (%s, %s)", (u"あう", u"to meet"))
    cursor.execute("INSERT INTO first_year_verb (word, meaning) VALUES (%s, %s)", (u"ある", u"there is"))
    cursor.execute("INSERT INTO first_year_verb (word, meaning) VALUES (%s, %s)", (u"かう", u"to buy"))
    cursor.execute("INSERT INTO first_year_verb (word, meaning) VALUES (%s, %s)", (u"かく", u"to write"))
    cursor.execute("INSERT INTO first_year_verb (word, meaning) VALUES (%s, %s)", (u"とる", u"to take (a picture)"))
    cursor.execute("INSERT INTO first_year_verb (word, meaning) VALUES (%s, %s)", (u"まつ", u"to wait"))
    cursor.execute("INSERT INTO first_year_verb (word, meaning) VALUES (%s, %s)", (u"わかる", u"to understand"))
    cursor.execute("INSERT INTO first_year_verb (word, meaning) VALUES (%s, %s)", (u"いる", u"(a person) is in"))
    cursor.execute("INSERT INTO first_year_verb (word, meaning) VALUES (%s, %s)", (u"およぐ", u"to swim"))
    cursor.execute("INSERT INTO first_year_verb (word, meaning) VALUES (%s, %s)", (u"きく", u"to ask"))
    cursor.execute("INSERT INTO first_year_verb (word, meaning) VALUES (%s, %s)", (u"のる", u"to ride"))
    cursor.execute("INSERT INTO first_year_verb (word, meaning) VALUES (%s, %s)", (u"やる", u"to do"))
    cursor.execute("INSERT INTO first_year_verb (word, meaning) VALUES (%s, %s)", (u"でかける", u"to go out"))
    cursor.execute("INSERT INTO first_year_verb (word, meaning) VALUES (%s, %s)", (u"あける", u"to open"))
    cursor.execute("INSERT INTO first_year_verb (word, meaning) VALUES (%s, %s)", (u"おしえる", u"to teach"))
    cursor.execute("INSERT INTO first_year_verb (word, meaning) VALUES (%s, %s)", (u"おりる", u"to get off"))
    cursor.execute("INSERT INTO first_year_verb (word, meaning) VALUES (%s, %s)", (u"かりる", u"to borrow"))
    cursor.execute("INSERT INTO first_year_verb (word, meaning) VALUES (%s, %s)", (u"しめる", u"to close"))
    cursor.execute("INSERT INTO first_year_verb (word, meaning) VALUES (%s, %s)", (u"シャワーをあびる", u"to take a shower"))
    cursor.execute("INSERT INTO first_year_verb (word, meaning) VALUES (%s, %s)", (u"つける", u"to turn on"))
    cursor.execute("INSERT INTO first_year_verb (word, meaning) VALUES (%s, %s)", (u"でんわをかける", u"to make a phone call"))
    cursor.execute("INSERT INTO first_year_verb (word, meaning) VALUES (%s, %s)", (u"わすれる", u"to forget"))
    cursor.execute("INSERT INTO first_year_verb (word, meaning) VALUES (%s, %s)", (u"うたう", u"to sing"))
    cursor.execute("INSERT INTO first_year_verb (word, meaning) VALUES (%s, %s)", (u"かぶる", u"to put on (hat)"))
    cursor.execute("INSERT INTO first_year_verb (word, meaning) VALUES (%s, %s)", (u"しる", u"to get to know"))
    cursor.execute("INSERT INTO first_year_verb (word, meaning) VALUES (%s, %s)", (u"すむ", u"to live"))
    cursor.execute("INSERT INTO first_year_verb (word, meaning) VALUES (%s, %s)", (u"はく", u"to put on (item below your waist)"))
    cursor.execute("INSERT INTO first_year_verb (word, meaning) VALUES (%s, %s)", (u"ふとる", u"to gain weight"))
    cursor.execute("INSERT INTO first_year_verb (word, meaning) VALUES (%s, %s)", (u"かける", u"to put on (glasses)"))
    cursor.execute("INSERT INTO first_year_verb (word, meaning) VALUES (%s, %s)", (u"きる", u"to put on (clothes above your waist)"))
    cursor.execute("INSERT INTO first_year_verb (word, meaning) VALUES (%s, %s)", (u"つとめる", u"to work for"))
    cursor.execute("INSERT INTO first_year_verb (word, meaning) VALUES (%s, %s)", (u"やせる", u"to be thin"))
    cursor.execute("INSERT INTO first_year_verb (word, meaning) VALUES (%s, %s)", (u"じろじろみる", u"to stare"))
    cursor.execute("INSERT INTO first_year_verb (word, meaning) VALUES (%s, %s)", (u"すてる", u"to throw away"))
    cursor.execute("INSERT INTO first_year_verb (word, meaning) VALUES (%s, %s)", (u"はじめる", u"to begin"))

    
    print("INSERTED DATA TO TABLE first_year_verb")
    database.commit()
    
#create_hiragana()
#create_specialform()
#create_ruverb()
create_verb()
