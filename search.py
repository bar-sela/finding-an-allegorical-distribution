import copy

###### מתואר למעטה הclass של node עם פונקציות רלוונטיות

##הפונקציה dfs בשביל סעיף א'
'''
 
בסעיף זה התבקשתי לממש חיפוש במרחב המצבים לבעיית חלוקת חפצים אליגיטרית בין 2 שחקנים עם הערכות זהות.
מיממשתי זאת על ידי בניית עץ מצבים וחיפוש בעץ במקביל(כלומר בלי לעבור על העץ פעמיים ) לעומק (dfs)כפי שאסביר למעטה :
האלגו' מקבל את גודל הרשימת חפצים,את הרשימה עצמה עם שווי החפצים, אבוייקט מסוג קודקוד שבנייתו מתוארת למעטה ואינדקס התחלתי 0 . 
בתור התחלה בשורות 22-23 מתוארת בניית עץ מצבים כאשר בכל נבנים 2 ילדים לקודקוד שאנחנו כרגע עליו : ילד אחד מקבע מצב שבו
החפץ שאנחנו כרגע דנים בו ילך לאדם א' וילד שני מקבע מצב שבה החפץ שאנחנו כרגע דנים בו ילך לילד ב' .
 לאחר מכן נמשיך בנייה לעומק כאשר הפונקציה חוזרת ברקורסיה עם האינדקס הבא שמשמעותו שדנים כעת בחפץ הבא ברשימה.
 הריצה תעצור כאשר נסיים את החפצים שלנו ותוחזר החלוקה שהוגדרה עד כה לפי המסלול שעברנו בעץ.
 בדרך חזרה במעלה העץ אנחנו מבררים איזה תת עץ "ניצח" מבחינת מינימום מקסימלי בחלוקה שהוא מגדיר, אם החלוקה שהגדיר תת העץ השמאלי ניצחה אז האבא יחזיר 
 את החלוקה שהגדיר תת העץ השמאלי ולהיפך כך שלבסוף נקבל את החלוקה האגליטירית. 

 '''
def dfs(listOfValues,sizeOflist,nodeRoot,index):
    if index == sizeOflist :
        print(nodeRoot.data)
        return  nodeRoot.data
    nodeRoot.createChildren()
    nodeRoot.insert(listOfValues,index)
    n1 = dfs(listOfValues, sizeOflist,nodeRoot.left ,index+1)
    n2 = dfs(listOfValues, sizeOflist,nodeRoot.right ,index+1)
    if min(n1) > min(n2) :
        return n1
    else:
        return n2

## בשביל סעיף ב'
## בסעיף זה בעזרת dfs2 מיממשתי את גיזום כלל א' .
'''
מאוד דומה למקודם מלבד הבדל אחד מהותי, תיהיה לנו רשימה בשם listOfSituations 
אשר תתחיל בתור רשימה ריקה ותוך כדי הבנייה/חיפוש לעומק שתיארנו קודם לכן בdfs אנחנו נשמור ברשימה הזו את כל המצבים שנתקלנו בהם עד כה, 
כך שאם נתקלנו במצב נוסף נדע להגיב בהתאם. לדוגמא בחלוקה 5,5,0 אם כבר יש לנו 5,5 אז כאשר הבן הימני של הבן הימני של שורש העץ יגדיר חלוקה נוספת של 5,5 (כיוון שיהיה לנו קיבוע נוסף של 5 שמופיע פעמיים)
אז במקרה כזה לא נקרא ברקורסיה את הפונקציה על הבן הימני של הבן הימני של שורש העץ .  
  


'''
def dfs2(listOfValues,sizeOflist,nodeRoot,index, listOfSituations ):
    if index == sizeOflist :
        print(nodeRoot.data)
        return  nodeRoot.data
    nodeRoot.createChildren()
    nodeRoot.insert(listOfValues, index)
    if nodeRoot.left.data not in listOfSituations :
        listOfSituations.append((copy.deepcopy(nodeRoot.left.data)))
        n1 = dfs2(listOfValues, sizeOflist, nodeRoot.left, index + 1,listOfSituations)
    else :
        n1 = nodeRoot.data
    if nodeRoot.right.data not in listOfSituations:
        listOfSituations.append((copy.deepcopy(nodeRoot.right.data)))
        n2 = dfs2(listOfValues, sizeOflist, nodeRoot.right, index + 1,listOfSituations)
    else :
       n2 = nodeRoot.data
        ### יש כאן טיפול במקרה קיצון של חפץ שהשווי שלו הוא 0 - במקרה כזה נדפיס את  nodeRoot.data
        #- כלומר נתייחס לקודקוד שאנחנו עליו כעלה למרות שניתן טכנית לקבע את הערך 0 לכל אחד מהבנים שלו אבל זה לא הכרחי
    if min(n1) > min(n2):
        if n1 == nodeRoot.data :
            print(nodeRoot.data)
        return n1
    else:
        if n2 == nodeRoot.data:
            print(nodeRoot.data)
        return n2








class Node:
   def __init__(self):
     self.left = None
     self.right  = None
     self.data = [0,0]
   def createChildren(self):
            self.left = Node()
            self.left.data = copy.deepcopy(self.data)
            self.right = Node()
            self.right.data = copy.deepcopy(self.data)
   def insert(self, listOfpartions, index ):
               self.left.data[0] += listOfpartions[index]
               self.right.data[1] += listOfpartions[index]



