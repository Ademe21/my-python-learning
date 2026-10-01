import sqlite3

ግንኙነት = sqlite3.connect("ትምህርት_ቤት.db")
አዛዥ = ግንኙነት.cursor()

# ትእዛዝ እንስጥ
አዛዥ.execute("SELECT * FROM ተማሪዎች")

# 1. fetchone() በመጠቀም የመጀመሪያውን ተማሪ ብቻ ማውጣት
አንድ_ተማሪ = አዛዥ.fetchone()

print("👤 የመጀመሪያው ተማሪ ብቻ፦")
print(አንድ_ተማሪ)

ግንኙነት.close()
