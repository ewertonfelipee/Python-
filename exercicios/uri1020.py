#Uri 1020

def age_in_days(age):
    
    year = 365
    
    month = year // 12
    
    days = month // 30
    
    p, q = divmod(age, year)
    
    print(p, f"ano(s)")
    
    r, s = divmod(q, month)
    
    print(r, f"mes(es)")
    
    t, v = divmod(s, days)
    
    print(t, f"dia(s)")
    
age_in_days(age = int(input()))