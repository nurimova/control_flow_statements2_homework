
# Xush kelibsiz  
# `elif` operatorlari bilan ishlash

Uyga vazifalar va test topshiriqlarini avtomatik baholash.  
- Ushbu repository'ni fork qiling.  
- Berilgan masalalarni yeching.  
- To'g'ri xabar bilan commit qiling.  

---

## Masalalar

### **if01**  
  Uchta son berilgan, ulardan eng kattasini toping.  

**Misol 1:**  
```Python
Input: a=1 b=4 c=2  
Output: 4  
```  

**Misol 2:**  
```Python
Input: a=-5 b=-3 c=-1  
Output: -1  
```  

**Cheklovlar:**  
- \(-10^{18} \leq son \leq 10^{18}\)

---

### **if02**  
  Uchta son berilgan, ulardan eng kichigini toping.  

**Misol 1:**  
```Python
Input: a=1 b=4 c=2  
Output: 1  
```  

**Misol 2:**  
```Python
Input: a=-5 b=-3 c=-1  
Output: -5  
```  

**Cheklovlar:**  
- \(-10^{18} \leq son \leq 10^{18}\)

---

### **if03**  
  Uchta sondan kattasi va kichigining orasidagi sonni aniqlang.  

**Misol 1:**  
```Python
Input: a=3 b=7 c=1  
Output: 3  
```  

**Misol 2:**  
```Python
Input: a=5 b=5 c=-1  
Output: 5  
```  

**Cheklovlar:**  
- \(-10^{18} \leq son \leq 10^{18}\)

---

### **if04**  
  Agar ikki son teng bo'lsa, 0 qaytaring, teng bo'lmasa, kattasini qaytaring.  

**Misol 1:**  
```Python
Input: a=3 b=7  
Output: 7  
```  

**Misol 2:**  
```Python
Input: a=5 b=5  
Output: 0  
```  

**Cheklovlar:**  
- \(-10^{18} \leq son \leq 10^{18}\)

---

### **if05**  
  Besh xonali sonning eng katta raqamini toping.  

**Misol 1:**  
```Python
Input: n=23546  
Output: 6  
```  

**Cheklovlar:**  
- \(-10^{18} \leq son \leq 10^{18}\)

---

### **if06**  
  Besh xonali sonning eng katta raqami qaysi o'rinda ekanini toping.  

**Misol 1:**  
```Python
Input: n=76514  
Output: 5  
```  

**Misol 2:**  
```Python
Input: a=54694  
Output: 2  
```  

**Cheklovlar:**  
- \(-10^{18} \leq son \leq 10^{18}\)

---

### **if07**  
  Celsius bo'yicha haroratni quyidagi shartlarga ko'ra aniqlang. `elif` operatorlarini ishlating:  
  - **Temp<0**: "Freezing"  
  - **1<=Temp<=10**: "Very Cold"  
  - **11<=Temp<=20**: "Cold"  
  - **21<=Temp<=30**: "Normal"  
  - **31<=Temp<=40**: "Hot"  
  - **Temp>40**: "Very Hot"  

**Misol 1:**  
```Python
Input: n=14  
Output: "Cold"  
```  

**Misol 2:**  
```Python
Input: a=-4  
Output: "Freezing"  
```  

**Cheklovlar:**  
- \(-10^{18} \leq son \leq 10^{18}\)

---

### **if08**  
  1 dan 7 gacha bo'lgan son berilgan. Unga mos ravishda haftaning kunini qaytaring. `elif` operatorlarini ishlating:  
  - **1**: "Monday"  
  - **2**: "Tuesday"  
  - **3**: "Wednesday"  
  - **4**: "Thursday"  
  - **5**: "Friday"  
  - **6**: "Saturday"  
  - **7**: "Sunday"  

**Misol 1:**  
```Python
Input: n=2  
Output: "Tuesday"  
```  

**Misol 2:**  
```Python
Input: a=6  
Output: "Saturday"  
```  

**Cheklovlar:**  
- \(-10^{18} \leq son \leq 10^{18}\)

---

**Eslatma:**  
- Boshqalarning echimlarini nusxalamang.  
- Izohlarni o'chirmang.  
