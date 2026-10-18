import sqlite3

# 1. ከዳታቤዝ ጋር መገናኘት እና ሰንጠረዥ ማዘጋጀት
ግንኙነት = sqlite3.connect("ትምህርት_ቤት.db")
አዛዥ = ግንኙነት.cursor()

አዛዥ.execute("""
CREATE TABLE IF NOT EXISTS ተማሪዎች (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    ስም TEXT NOT NULL,
    እድሜ INTEGER,
    ክፍል TEXT
)
""")
ግንኙነት.commit()

# 2. የፕሮግራሙ ዋና አየር መንገድ (Menu Loop)
while True:
    print("\n--- 📚 የተማሪዎች መዝገብ ቤት ---")
    print("1. አዲስ ተማሪ መመዝገብ")
    print("2. ሁሉንም ተማሪዎች ማየት")
    print("3. የተማሪ ክፍል ማሻሻል")
    print("4. ተማሪ መሰረዝ")
    print("5. ከፕሮግራሙ ወጣ")
    
    ምርጫ = input("እባክህ ከ 1-5 ያለውን ቁጥር ምረጥ፦ ")
    
    # 1. አዲስ ተማሪ መጨመር (INSERT)
    if ምርጫ == "1":
        ስም = input("የተማሪ ስም፦ ")
        እድሜ = int(input("እድሜ፦ "))
        ክፍል = input("ክፍል፦ ")
        
        አዛዥ.execute("INSERT INTO ተማሪዎች (ስም, እድሜ, ክፍል) VALUES (?, ?, ?)", (ስም, እድሜ, ክፍል))
        ግንኙነት.commit()
        print("✅ ተማሪው በስኬት ተመዝግቧል!")
        
    # 2. ተማሪዎችን በሙሉ ማየት (SELECT)
    elif ምርጫ == "2":
        አዛዥ.execute("SELECT * FROM ተማሪዎች")
        ተማሪዎች = አዛዥ.fetchall()
        
        print("\n📋 የተመዘገቡ ተማሪዎች ዝርዝር፦")
        for ተማሪ in ተማሪዎች:
            print(f"ID: {ተማሪ[0]} | ስም: {ተማሪ[1]} | እድሜ: {ተማሪ[2]} | ክፍል: {ተማሪ[3]}")
            
    # 3. መረጃ ማሻሻል (UPDATE)
    elif ምርጫ == "3":
        ተማሪ_id = int(input("ማስተካከል የምትፈልገውን የተማሪ ID አስገባ፦ "))
        አዲስ_ክፍል = input("አዲሱን ክፍል አስገባ፦ ")
        
        አዛዥ.execute("UPDATE ተማሪዎች SET ክፍል = ? WHERE id = ?", (አዲስ_ክፍል, ተማሪ_id))
        ግንኙነት.commit()
        print("✅ የተማሪው ክፍል ተሻሽሏል!")
        
    # 4. መረጃ መሰረዝ (DELETE)
    elif ምርጫ == "4":
        ተማሪ_id = int(input("መሰረዝ የምትፈልገውን የተማሪ ID አስገባ፦ "))
        
        አዛዥ.execute("DELETE FROM ተማሪዎች WHERE id = ?", (ተማሪ_id,))
        ግንኙነት.commit()
        print("🗑️ የተማሪው መረጃ ተሰርዟል!")
        
    # 5. መውጫ
    elif ምርጫ == "5":
        print("👋 ደህና ሁን!")
        break
    else:
        print("❌ የተሳሳተ ምርጫ! እባክህ ከ 1 እስከ 5 ያለውን ቁጥር ምረጥ።")

# ግንኙነቱን መዝጋት
ግንኙነት.close()