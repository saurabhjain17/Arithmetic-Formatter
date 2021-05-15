def arithmetic_arranger(problems,output=None):
    if len(problems)>5:
      return "Error: Too many problems."
    first=[]
    operator=[]
    last=[]  
    for i in problems  :
        if "+" not in i and "-" not in i:
          return "Error: Operator must be '+' or '-'."
        else:
           if "+" in i:
             first.append(i[:i.index("+")-1])
             last.append(i[i.index("+")+2:])  
             operator.append("+")
             if len(first[-1])>4 or len(last[-1])>4:
                return "Error: Numbers cannot be more than four digits."
             if first[-1].isdigit()==False or last[-1].isdigit()==False:
               return "Error: Numbers must only contain digits."   
           elif "-" in i: 
             first.append(i[:i.index("-")-1])
             last.append(i[i.index("-")+2:])  
             operator.append("-")  
             if len(first[-1])>4 or len(last[-1])>4:
                return "Error: Numbers cannot be more than four digits."
             if first[-1].isdigit()==False or last[-1].isdigit()==False:
               return "Error: Numbers must only contain digits."  
    first1="  "
    last1=""
    ans=""
    line=""
    for i in range(len(operator)):           
          dis=(len(first[i])-len(last[i]))
          if dis>=0:
            first1=first1+first[i]+" "*6
            last1=last1+operator[i]+" "*(dis+1)+last[i]+" "*4
            line=line+ "-"*(max(len(first[i]),len(last[i]))+2)+" "*4
          if dis<0:
            first1=first1+" "*abs(dis)+first[i]+" "*6
            last1=last1+operator[i]+" "+last[i]+" "*4
            line=line+ "-"*(max(len(first[i]),len(last[i]))+2)+" "*4              
          if operator[i]=="+":
             m=str(int(first[i])+int(last[i]))
          if operator[i]=="-":
             m=str(int(first[i])-int(last[i])) 
          ans=ans+" "*((max(len(first[i]),len(last[i]))+2)-len(m))+m+" "*4 
    if output==True:      
        arranged_problems=first1[:-6]+"\n"+last1[:-4]+"\n"+line[:-4]+"\n"+ans[:-4]  
    if output==None:         
         arranged_problems=first1[:-6]+"\n"+last1[:-4]+"\n"+line[:-4] 
    return arranged_problems
