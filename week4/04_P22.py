x=input().replace("0"," zero ").replace("9"," nine ").replace("8"," eight ").replace("7"," seven ").replace("6"," six ").replace("5"," five ").replace("4"," four ").replace("3"," three ").replace("2"," two ").replace("1"," one ")
for i in ["zero","one","two","three","four","five","six","seven","eight","nine"]:
    x=x.replace("  "+i," "+i).replace(i+"  ",i+" ").replace("- "+i,"-"+i).replace(i+" -",i+"-").replace("ext "+i,"ext"+i)
print(x)
