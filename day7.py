import sqlite3

ግንኙነት = sqlite3.connect("ትምህርት_ቤት.db")
አዛዥ = ግንኙነት.cursor()

# 1. አንዱን ተማሪ በ ID ብቻ ለመፈለግ (አንድ እቃ ብቻ ሲኖር)
ተማሪ_id = 1

# ኮማን በመጠቀም (ትክክለኛው የቱፕል አሰራር)
አዛዥ.execute("SELECT * FROM ተማሪዎች WHERE id = ?", (ተማሪ_id,))
результаት = አዛዥ.fetchone()

print("የተገኘው ተማሪ፦", результат)

ግንኙነት.close()