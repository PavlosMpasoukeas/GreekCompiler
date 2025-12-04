import sys
import os


alphabet =['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q',
'R','S','T','U','V','W','X','Y','Z','a','b','c','d','e','f','g','h','i','j','k',
'l','m','n','o','p','q','r','s','t','u','v','w','x','y','z',
'Α','Β','Γ','Δ','Ε','Ζ','Η','Θ','Ι','Κ','Λ','Μ','Ν','Ξ','Ο','Π','Ρ','Σ','Τ','Υ','Φ','Χ','Ψ','Ω',
'Ά','Έ','Ή','Ί','Ό','Ύ','Ώ',
'α','β','γ','δ','ε','ζ','η','θ','ι','κ','λ','μ','ν','ξ','ο','π','ρ','σ','τ','υ','φ','χ','ψ','ω','ς',
'ά','έ','ή','ί','ό','ύ','ώ']
numbers=['0','1','2','3','4','5','6','7','8','9']

file= open(sys.argv[1],'r',encoding='utf-8')

#xaraktires sto automato
space=0
tab=1
nextline=2
number=3
letter=4
comma=5
anokatotel=6
katopaula=7
questionmark=8
left_parenth=9
right_parenth=10
left_aggili=11
right_aggili=12                                                   
opencomment=13
closecomment=14
equal=15
less_than=16
greater_than=17
plus=18
minus=19
multi=20
divide=21
mod=22   # %
eof=23
allo_sumbolo=24


#katastaseis
kat_start=0
kat_number=1
kat_letter=2
kat_anokatotel=3
kat_lessthan=4
kat_greaterthan=5
kat_comments=6

#tokens
id_token=100
number_token=102
comma_token=103
anokatotel_token=104
questionmark_token=105
left_parenth_token=106
right_parenth_token=107
left_aggili_token=108
right_aggili_token=109
opencomments_token=110
closecomments_token=111
equal_token=112
lessthan_token=113
greaterthan_token=114
lessORequal_token=115
greaterORequal_token=116
plus_token=117
minus_token=118
multi_token=119
divide_token=120
mod_token=121
eof_token=122
anathesi_token=123
diaforo_token=124


#Δεσμευμενες λεξεις

program_token=500
if_token=501
repeat_token=502
for_token=503
read_token=504
function_token=505
in_token=506
start_function_token=507
start_procedure_token=508
start_program_token=509
or_token=510
decleration_token=511   #δηλωση
then_token=512         #τοτε
until_token=513         #μεχρι
to_token=514            #εως
wright_token=515
procedure_token=516
out_token=517
and_token=518
else_token=519
while_token=520
step_token=521
interface_token=522
end_function_token=523
end_procedure_token=524
end_program_token=525
execute_token=_token=526
endif_token=527
endwhile_token=528
endfor_token=529
not_token=530

#error
error_not_acceptable_symbol=1000
error_over_30_char=1001
error_katopaula=1002    #otan einai kato paula moni tis
error_num_letter=1003   #otan einai arithmos kai meta gramma
error_OpenCommentsWithEOF=1004
error_only_close_comment=1005  #otan yparxei mono deksi aggistro


array_transitions = [
      #kat_start
      [kat_start,kat_start,kat_start,kat_number,kat_letter,comma_token,kat_anokatotel,error_katopaula,
       questionmark_token,left_parenth_token,right_parenth_token,left_aggili_token,right_aggili_token,kat_comments,
       error_only_close_comment,equal_token,kat_lessthan,kat_greaterthan,plus_token,minus_token,multi_token,
       divide_token,mod_token,eof_token,error_not_acceptable_symbol],


      #kat_number
      [number_token,number_token,number_token,kat_number,error_num_letter,number_token,number_token,
       number_token,number_token,number_token,number_token,number_token,number_token,number_token,number_token,
       number_token,number_token,number_token,number_token,number_token,number_token,number_token,number_token,
       number_token,error_not_acceptable_symbol],

      #kat_letter
      [id_token,id_token,id_token,kat_letter,kat_letter,id_token,id_token,kat_letter,id_token,id_token,
       id_token,id_token,id_token,id_token,id_token,id_token,id_token,id_token,id_token,id_token,id_token,id_token,
       id_token,id_token,error_not_acceptable_symbol],


      #kat_anokatotel
      [anokatotel_token,anokatotel_token,anokatotel_token,anokatotel_token,anokatotel_token,
       anokatotel_token,anokatotel_token,anokatotel_token,anokatotel_token,anokatotel_token,anokatotel_token,
       anokatotel_token,anokatotel_token,anokatotel_token,anokatotel_token,anathesi_token,anokatotel_token,
       anokatotel_token,anokatotel_token,anokatotel_token,anokatotel_token,anokatotel_token,anokatotel_token,
       anokatotel_token,error_not_acceptable_symbol],



      #kat_lessthan
      [lessthan_token,lessthan_token,lessthan_token,lessthan_token,lessthan_token,lessthan_token,
       lessthan_token,lessthan_token,lessthan_token,lessthan_token,lessthan_token,lessthan_token,lessthan_token,
       lessthan_token,lessthan_token,lessORequal_token,lessthan_token,diaforo_token,lessthan_token,lessthan_token,
       lessthan_token,lessthan_token,lessthan_token,lessthan_token,error_not_acceptable_symbol],


      #kat_greaterthan
      [greaterthan_token,greaterthan_token,greaterthan_token,greaterthan_token,greaterthan_token,
       greaterthan_token,greaterthan_token,greaterthan_token,greaterthan_token,greaterthan_token,greaterthan_token,
       greaterthan_token,greaterthan_token,greaterthan_token,greaterthan_token,greaterORequal_token,greaterthan_token,
       greaterthan_token,greaterthan_token,greaterthan_token,greaterthan_token,greaterthan_token,greaterthan_token,
       greaterthan_token,error_not_acceptable_symbol],


      #kat_comments
      [kat_comments,kat_comments,kat_comments,kat_comments,kat_comments,kat_comments,kat_comments,
       kat_comments,kat_comments,kat_comments,kat_comments,kat_comments,kat_comments,kat_comments,kat_start,
       kat_comments,kat_comments,kat_comments,kat_comments,kat_comments,kat_comments,kat_comments,kat_comments,
       error_OpenCommentsWithEOF,kat_comments]
       
]  

 
line = 1  #current line

def lex():
    global line
    token_str=''
    p=kat_start #katastasi pou vriskomaste tora
    res=[]
    linecounter=line
    
    while(p>=0 and p<=6):
        reader = file.read(1) #read 1 character from the file
        
        if(reader == ' '):
            tk = space
        elif(reader == '\t'):
            tk = tab
        elif(reader == '\n'):
            linecounter=linecounter+1
            tk = nextline
        elif(reader in numbers):
            tk = number
        elif(reader in alphabet):
            tk = letter
        elif(reader == ','):
            tk = comma
        elif(reader == ':'):
            tk = anokatotel
        elif(reader == '_'):
            tk = katopaula
        elif(reader == ';'):
            tk = questionmark
        elif(reader == '('):
             tk = left_parenth
        elif(reader == ')'):
             tk = right_parenth
        elif(reader == '['):
             tk = left_aggili
        elif(reader == ']'):
             tk = right_aggili
        elif(reader == '{'):
             tk = opencomment
        elif(reader == '}'):
             tk = closecomment
        elif(reader == '='):
             tk = equal
        elif(reader == '<'):
             tk = less_than
        elif(reader == '>'):
             tk = greater_than
        elif(reader == '+'):
             tk = plus
        elif(reader == '-'):
             tk = minus
        elif(reader == '*'):
             tk = multi
        elif(reader == '/'):
             tk = divide
        elif(reader == '%'):
             tk = mod
        elif(reader == ''):
             tk = eof
        else:
             tk = allo_sumbolo
             
        
        
        p = array_transitions[p][tk]
        y = len(token_str)    
        
        
   
        if(y<30):
            if(p!=kat_start and p!=kat_comments):
                token_str+=reader
        else:
            p = error_over_30_char
            
    

    if(p == number_token or p == id_token or p == lessthan_token or p == greaterthan_token or p == anokatotel_token):
        if(reader == '\n'):
            linecounter -= 1
        file.seek(file.tell()-1,0)
        token_str = token_str[:-1]
    
    if(p == id_token):
        if(token_str == 'πρόγραμμα'):
            p = program_token
        elif(token_str == 'εάν'):
            p = if_token
        elif(token_str == 'επανάλαβε'):
            p = repeat_token
        elif(token_str == 'για'):
            p = for_token
        elif(token_str == 'διάβασε'):
            p = read_token
        elif(token_str == 'συνάρτηση'):
            p = function_token
        elif(token_str == 'είσοδος'):
            p = in_token
        elif(token_str == 'αρχή_συνάρτησης'):
            p = start_function_token
        elif(token_str == 'αρχή_διαδικασίας'):
            p = start_procedure_token
        elif(token_str == 'αρχή_προγράμματος'):
            p = start_program_token
        elif(token_str == 'ή'):
            p = or_token
        elif(token_str == 'δήλωση'):
            p = decleration_token
        elif(token_str == 'τότε'):
            p = then_token
        elif(token_str == 'μέχρι'):
            p = until_token
        elif(token_str == 'έως'):
            p = to_token
        elif(token_str == 'γράψε'):
            p = wright_token
        elif(token_str == 'διαδικασία'):
            p = procedure_token
        elif(token_str == 'έξοδος'):
            p = out_token
        elif(token_str == 'και'):
            p = and_token
        elif(token_str == 'αλλιώς'):
            p = else_token
        elif(token_str == 'όσο'):
            p = while_token
        elif(token_str == 'με_βήμα'):
            p = step_token
        elif(token_str == 'διαπροσωπεία'):
            p = interface_token
        elif(token_str == 'τέλος_συνάρτησης'):
            p = end_function_token
        elif(token_str == 'τέλος_διαδικασίας'):
            p = end_procedure_token
        elif(token_str == 'τέλος_προγράμματος'):
            p = end_program_token
        elif(token_str == 'εκτέλεσε'):
            p = execute_token
        elif(token_str == 'εάν_τέλος'):
            p = endif_token
        elif(token_str == 'όσο_τέλος'):
            p = endwhile_token
        elif(token_str == 'για_τέλος'):
            p = endfor_token 
        elif(token_str == 'όχι'):
            p = not_token  

    #error check
    if(p == error_not_acceptable_symbol):
        print("ERROR: Στην γραμμή %d υπάρχει το μη αποδεκτό σύμβολο %s" %(line, reader))
    elif(p == error_over_30_char):
        print("ERROR: Η λέξη %d στην γραμμή &s ξεπερνά τους 30 χαρακτήρες" %(reader, line))
    elif(p == error_katopaula):
        print("ERROR: Στην γραμμή %d , ο χαρακτήρας << _ >> δεν υποστηρίζεται μόνος του" %(line))        
    elif(p == error_num_letter):
        print("ERROR: Στην γραμμή %d . Δεν μπορεί να ακολουθεί γράμμα μετά από κάποιο ψηφίο" %(line))        
    elif(p == error_OpenCommentsWithEOF):
        print("ERROR: Missing << } >>, δεν έκλεισαν τα σχόλια στο τέλος του αρχείου")        
    elif(p == error_only_close_comment):
        print("ERROR: Στην γραμμή %d , ο χαρακτήρας << } >> δεν υποστηρίζεται μόνος του" %(line))  

    if(p == number_token):
        if(int(token_str) > 32767):
            p = ERROR_NUMBER_OVER_LIMIT
            
            
    
    
    res.append(p)
    res.append(token_str)
    res.append(linecounter)
    line=linecounter

    
    return res 

#telos lektikou analuth

     

#synartiseis endiamesou 

global totalQuads
quadCounter = 1       #arithmos tetradas
totalQuads = []
T_n = 1               #arithmos tis temp metavlitis
totalQuadsTeliko = []
def nextquad():#epistrefei arithmo 4adas
    global quadCounter
    
    return quadCounter


def genquad(op, x, y, z):
    global quadCounter
    global totalQuads
    global totalQuadsTeliko
    
    
    list = []
    list += [quadCounter] + [op] + [x] + [y] + [z]
    quadCounter += 1
    totalQuads += [list]
    totalQuadsTeliko += [list]
    
    return list


def newtemp():#dhmiourgei nea proswrinh metalbhth
    global T_n
    global VarList
    
    
    Var = "T@" + str(T_n)
    T_n += 1
    
    ent = Entity()
    ent.type = 'TEMP'
    ent.name = Var
    ent.tempvar.offset = compute_offset()
    new_entity(ent)
    
    return Var
    
    
def emptylist():
    
    return []

def makelist(x):#επιστρεφει μια λιστα ετικετων 4αδων που περιεχει μονο το x
    
    return [x]
    
def merge(list1, list2):#επιστρεφει συνενωση των ετικετων των 4αδων των 2 λιστων
    
    return list1 + list2

def backpatch(list, z):#η λιστα list αποτελειται απο 4αδες της totalQuads που δεν εχουν συμπληρωμενο στοιχειο
    global totalQuads  #και συμπληρωνονται με την ετικετα z
    for i in range(len(list)):
        for j in range(len(totalQuads)):
            if list[i]==totalQuads[j][0]:#αν η 4αδα υπαρχει σαυτη τη λιστα συμπληρωνω το τελευταιο τηs στοιχειο με z
               totalQuads[j][4] = z
               break;
            
    return
   

#pinakas_simvolon



class Scope():
    def __init__(self):
        self.name = ''
        self.entityList = []
        self.nestingLevel = 0
scopelist = [] #ola ta scopes

class Entity():
    def __init__(self):
        self.name = ''
        self.type = ''   #var, subprogram, param, T@
        
        self.var = self.Variable()
        self.subprogram = self.SubProgram()
        self.param = self.Parameter()
        self.tempvar = self.TempVar()
    
    class Variable():
        def __init__(self):
            self.type = 'int'
            self.offset = 0
    
    class SubProgram():
        def __init__(self):
            self.type = ''        #proc or func
            self.startQuad = 0
            self.argumentList = []
            self.frameLength = 0
            self.nestingLevel = 0
    
    class Parameter:
        def __init__(self):
            self.mode = ''      #cv or ref
            self.offset = 0
    
    class TempVar():
        def __init__(self):
            self.type = 'int'
            self.offset = 0

class Argument():
    def __init__(self):
        self.name = ''
        self.type = 'int'
        self.parMode = ''    #cv or ref

'''καλειται στα programblock funcblock procblock'''
def new_scope(name):#dhmiourgw neo scope
    global scopelist
    
    nextScope = Scope()
    nextScope.name = name
    if(not scopelist):#an scopelist adeia benei san scope main programm
        nextScope.nestingLevel = 0
    else:
         nextScope.nestingLevel = scopelist[-1].nestingLevel + 1#alliws benei akribws apo panw apto pio prosfato scope ths listas
         
    scopelist.append(nextScope)#to prosthetw sto telos ths listas
    
'''καλειται στα programblock funcblock procblock'''    
def delete_scope():
    global scopelist
    
    freeScope = scopelist.pop()
    del freeScope
    
'''καλειται στα add_parameters newtemp varlist proc func'''
def new_entity(object):
    global scopelist
    scopelist[-1].entityList.append(object)#prosthetei kainourgia odotita sto telos tis listas entities TOY TELEFTAIOU SCOPE
    
'''καλειται στα varlist'''
def new_argument(object):
    global scopelist
    #prosthetei kai dhmiourgei ena neo argument sto telefteo entity sto telefteo scope
    scopelist[-1].entityList[-1].subprogram.argumentList.append(object)

'''καλειται στα newtemp compute_frameLength add_parameters varlist'''
def compute_offset():#upologizei to offset afou exoun prostethei ola ta entities enos scope
    global scopelist
    
    counter = 0
    if(scopelist[-1].entityList is not[]):
        for ent in (scopelist[-1].entityList):
            if(ent.type == 'VAR' or ent.type == 'TEMP' or ent.type == 'PARAM'):
                counter += 1
    offset = 12+(counter*4)
    
    return offset

'''καλειται στα funcblock procblock'''
def compute_startQuad():#βρισκει την αρχικη 4αδα ενος subprogram
    global scopelist
    
    scopelist[-2].entityList[-1].subprogram.startQuad = nextquad()
    
'''καλειται στα funcblock procblock'''    
def compute_frameLength():#βρισκει τo frameLength
    global scopelist
    
    scopelist[-2].entityList[-1].subprogram.frameLength = compute_offset()

'''καλειται στα funcblock procblock'''
def add_parameters():#prosthetei parametro se entity pou einai subprogram
    global scopelist
    
    for arg in scopelist[-2].entityList[-1].subprogram.argumentList:
        ent = Entity()
        ent.name = arg.name
        ent.type = 'PARAM'
        ent.param.mode = arg.parMode
        ent.param.offset = compute_offset()
        new_entity(ent)

'''καλειται στα programblock funcblock procblock'''
def print_SYMPOL_TABLE():
    global scopelist
    global symFile
    
    symFile.write("------------------------------------")
    symFile.write("\n")
    
    for scop in reversed(scopelist):
        symFile.write("SCOPE: "+"name:"+scop.name+" nestingLevel:"+str(scop.nestingLevel))
        symFile.write("\n\tENTITIES:\n")
        for ent in scop.entityList:
            if(ent.type == 'VAR'):
                symFile.write("\tENTITY: "+" name:"+ent.name+"\t type:"+ent.type+"\t variable-type:"+ent.var.type+"\t offset:"+str(ent.var.offset))
            elif(ent.type == 'TEMP'):
                symFile.write("\tENTITY: "+" name:"+ent.name+"\t type:"+ent.type+"\t temp-type:"+ent.tempvar.type+"\t offset:"+str(ent.tempvar.offset))
            elif(ent.type == 'SUBPR'):
                symFile.write("\tENTITY: "+" name:"+ent.name+"\t type:"+ent.type+"\t subprogram-type:"+ent.subprogram.type+"\t startQuad:"+str(ent.subprogram.startQuad)+"\t frameLength:"+str(ent.subprogram.frameLength))
                symFile.write("\t\tARGUMENTS:")
                for arg in ent.subprogram.argumentList:
                    symFile.write("\t\tARGUMENT: "+" name:"+arg.name+"\t type:"+arg.type+"\t parMode:"+arg.parMode)
            elif(ent.type == 'PARAM'):
                symFile.write("\tENTITY: "+" name:"+ent.name+"\t type:"+ent.type+"\t mode:"+ent.param.mode+"\t offset:"+str(ent.param.offset))
            symFile.write("\n")
        symFile.write("\n\n")
    symFile.write("---------------------------------")
    symFile.write("\n\n\n\n\n")

'''καλειται στα loadvr storerv gnlvcode Telikos'''
def search_entity(k):#ψαχνει να βρει αν η οντοτητα με ονομα κ βρισκεται σε καποιο scope
        global scopelist
        
        for scope in reversed(scopelist):
            for entity in scope.entityList:
                if(entity.name == k):
                    return (scope,entity)
        print("Η οντότητα με όνομα " + str(k) + " δεν υπάρχει στον πίνακα συμβόλων")
        exit(0)
#TELIKOS

TelFile = open('TelFile.asm','w')
TelFile.write('         \n\n')



def loadvr(v,r):
    global scopelist
    global TelFile
    
    if v.isdigit():#a  h metavlith einai psifio
        TelFile.write('li t%d,%s\n' % (r,v))
    else:
        (sco,entit) = search_entity(v)#alliws psakse gia thn metavlhth kai epestrepse thn idia me to scope ths
        
        if sco.nestingLevel==0 and entit.type=='VAR':#an anikei sto scope tou main programma
            TelFile.write('lw t%d,-%d(gp)\n' % (r,entit.var.offset))
        
        elif sco.nestingLevel==scopelist[-1].nestingLevel:#an einai sto trexon scope  
            if entit.type=='VAR':#topikh metavlhth
                TelFile.write('lw t%d,-%d(sp)\n' % (r,entit.var.offset))
            
            elif entit.type=='TEMP':#proswrinh metavlhth
                TelFile.write('lw t%d,-%d(sp)\n' % (r,entit.tempvar.offset))
            
            elif entit.type=='PARAM' and entit.param.mode=='CV':#perasma me timh  
                TelFile.write('lw t%d,-%d(sp)\n' % (r,entit.param.offset))
            
            elif entit.type=='PARAM' and entit.param.mode=='REF':#perasma me anafora
                TelFile.write('lw t0,-%d(sp)\n' % (entit.param.offset))
                TelFile.write('lw t%d,(t0)\n' % (r))
            
        elif sco.nestingLevel < scopelist[-1].nestingLevel:#AN v exei dilwthei se kapoion progono 
                if entit.type=='VAR':#kai ekei einai topikh metavlhth
                    gnlvcode(v)
                    TelFile.write('lw t%d,(t0)\n' % (r))
                    
                elif entit.type=='PARAM' and entit.param.mode=='CV':#kai ekei einai paramteros pou pernaei me timh
                    gnlvcode(v)
                    TelFile.write('lw t%d,(t0)\n' % (r))
                
                elif entit.type=='PARAM' and entit.param.mode=='REF':#kai ekei einai parametros pou pernaei me anafora
                    gnlvcode(v)
                    TelFile.write('lw t0,(t0)\n')
                    TelFile.write('lw t%d,(t0)\n' % (r))

def storerv(r,v):
    global scopelist
    global TelFile
    
    (sco,entit)=search_entity(v)
    
    if sco.nestingLevel==0 and entit.type=='VAR':#An h v brisketai sto kurio programma
        TelFile.write('sw t%d,-%d(gp)\n' % (r,entit.var.offset))
    
    elif sco.nestingLevel == scopelist[-1].nestingLevel:#An h v brisketai sto trexon scope
        if entit.type=='VAR':#an einai metalbhth
            TelFile.write('sw t%d,-%d(sp)\n' % (r,entit.var.offset))
        
        elif entit.type=='TEMP':#an einai proswrinh metavlhth
            TelFile.write('sw t%d,-%d(sp)\n' % (r,entit.tempvar.offset))
        
        elif entit.type=='PARAM' and entit.param.mode=='CV':#an einai parametros me timh
            TelFile.write('sw t%d,-%d(sp)\n' % (r,entit.param.offset))
        
        elif entit.type=='PARAM' and entit.param.mode=='REF':#an einai parametros me anafora
            TelFile.write('lw t0,-%d(sp)\n' % (entit.param.offset))
            TelFile.write('sw t%d,(t0)\n' % (r))
     
    elif sco.nestingLevel < scopelist[-1].nestingLevel:#An v exei dhlwthei se kapoion progono 
        if entit.type=='VAR':#kai ekei einai topikh metavlhth
            gnlvcode(v)
            TelFile.write('sw t%d,(t0)\n' % (r))
        
        elif entit.type=='PARAM' and entit.param.mode=='CV':#kai ekei einai parametros me timh 
            gnlvcode(v)
            TelFile.write('sw t%d,(t0)\n' % (r))
         
        elif entit.type=='PARAM' and entit.param.mode=='REF':#kai ekei einai parametros me anafora
            gnlvcode(v)
            TelFile.write('lw t0,(t0)\n')
            TelFile.write('sw t%d,(t0)\n' % (r))
        


def gnlvcode(name):#εχει σκοπο να μεταφερει στον t0 την διευθυνση μιας ΜΗ τοπικης μεταβλητής 
    global scopelist
    global TelFile
    
    TelFile.write('lw t0,-4(sp)\n')
    (sco,entit)=search_entity(name)
    
    anc = scopelist[-1].nestingLevel - sco.nestingLevel;#ψαχνει στον πινακα συμβολων ποσα επιπεδα πανω βρισκεται αυτη η μη τοπικη μεταβλητη
    anc = anc - 1
    
    for i in range(0,anc):#ψαχνει σε ποιον προγονο βρισκεται η μεταβλητη
        TelFile.write('lw t0,-4(t0)\n')
        
    if entit.type=='VAR':
        e=entit.var.offset
    elif entit.type=='PARAM':
        e=entit.param.offset
        
    TelFile.write('addi t0,t0,-%d\n' % (e))

        
def search_call(i):#ψαχνει να βρει τις 4αδες που εκτελουν call
    global totalQuads#ωστε να επιστρεφει το καταλληλο υποπρογραμμα που θα κληθει
    
    start=i
    while start>=i:
        if(totalQuads[start][1]=='call'):
            return str(totalQuads[start][2])#επιστρεφει ονομα της συναρτησησς
        
        start=start+1
        
i_s=-1        


def Telikos():#θα καλειτε παντα μετα το end_block και πριν το delete_scope
    global scopelist#αφου δλδ τελειωνει μια συναρτηση και πριν διαγραψω το ψηλοτερο scope
    global totalQuads, i_s
    global TelFile
    
    for i in range(len(totalQuads)):
        TelFile.write('L' + str(totalQuads[i][0]) + ': \n')
        
        if(totalQuads[i][1] == 'jump'):
            TelFile.write('b L'+str(totalQuads[i][4])+'\n')
        
        elif(totalQuads[i][1] == '='):
            loadvr(totalQuads[i][2],1)
            loadvr(totalQuads[i][3],2)
            TelFile.write('beq,t1,t2,L'+str(totalQuads[i][4])+'\n')
         
        elif(totalQuads[i][1] == '<>'):
            loadvr(totalQuads[i][2],1)
            loadvr(totalQuads[i][3],2)
            TelFile.write('bne,t1,t2,L'+str(totalQuads[i][4])+'\n')
        
        elif(totalQuads[i][1] == '<'):
            loadvr(totalQuads[i][2],1)
            loadvr(totalQuads[i][3],2)
            TelFile.write('blt,t1,t2,L'+str(totalQuads[i][4])+'\n')
        
        elif(totalQuads[i][1] == '<='):
            loadvr(totalQuads[i][2],1)
            loadvr(totalQuads[i][3],2)
            TelFile.write('ble,t1,t2,L'+str(totalQuads[i][4])+'\n')
         
        elif(totalQuads[i][1] == '>'):
            loadvr(totalQuads[i][2],1)
            loadvr(totalQuads[i][3],2)
            TelFile.write('bgt,t1,t2,L'+str(totalQuads[i][4])+'\n')
        
          
        elif(totalQuads[i][1] == '>='):
            loadvr(totalQuads[i][2],1)
            loadvr(totalQuads[i][3],2)
            TelFile.write('bge,t1,t2,L'+str(totalQuads[i][4])+'\n')
        
        elif(totalQuads[i][1] == ':='):
            loadvr(totalQuads[i][2],1)
            storerv(1,totalQuads[i][4])
        
        elif(totalQuads[i][1] == '+'):
            loadvr(totalQuads[i][2],1)
            loadvr(totalQuads[i][3],2)
            TelFile.write('add,t1,t1,t2'+'\n')
            storerv(1,totalQuads[i][4])
         
        elif(totalQuads[i][1] == '-'):
            loadvr(totalQuads[i][2],1)
            loadvr(totalQuads[i][3],2)
            TelFile.write('sub,t1,t1,t2'+'\n')
            storerv(1,totalQuads[i][4])
     
        elif(totalQuads[i][1] == '*'):
            loadvr(totalQuads[i][2],1)
            loadvr(totalQuads[i][3],2)
            TelFile.write('mul,t1,t1,t2'+'\n')
            storerv(1,totalQuads[i][4])
        
        elif(totalQuads[i][1] == '/'):
            loadvr(totalQuads[i][2],1)
            loadvr(totalQuads[i][3],2)
            TelFile.write('div,t1,t1,t2'+'\n')
            storerv(1,totalQuads[i][4])
        
        elif(totalQuads[i][1] == 'inp'):
            TelFile.write('li a7,5'+'\n')
            TelFile.write('ecall'+'\n')
            TelFile.write('mv t1,a0'+'\n')#giana diavastei apto pliktrologio kai na topothetithei                  
            storerv(1,totalQuads[i][2])
        
        elif(totalQuads[i][1] == 'out'):
            loadvr(totalQuads[i][2],1)
            TelFile.write('mv a0,t1'+'\n')#na topothetithei pisw ston ti
            TelFile.write('li a7,1'+'\n')
            TelFile.write('ecall'+'\n')
        
        elif(totalQuads[i][1] == 'par'):
            if i_s==-1:#AN EINAI H PRWTH par     
                nsearch = search_call(i)
                (sco,entit)=search_entity(nsearch)
                TelFile.write('addi fp,sp,%d\n' % (entit.subprogram.frameLength))
                i_s=0
            
            if(totalQuads[i][3] == 'CV'):#an einai parametro me timh
                loadvr(totalQuads[i][2],0)
                TelFile.write('sw t0,-%d(fp)\n' % (12+4*i_s))
                i_s=i_s+1
            
            elif(totalQuads[i][3] == 'RET'):
                (sco,entit)=search_entity(totalQuads[i][2])
                TelFile.write('addi t0,sp,-%d\n' % (entit.tempvar.offset))
                TelFile.write('sw t0,-8(fp)\n')
             
            elif(totalQuads[i][3] == 'REF'):
                (sco,entit)=search_entity(totalQuads[i][2])
                
                if sco.nestingLevel==scopelist[-1].nestingLevel:
                    if entit.type=='VAR':
                        TelFile.write('addi t0,sp,-%d\n' % (entit.var.offset))
                        TelFile.write('sw t0,-%d(fp)\n' % (12+4*i_s))
                    
                    elif entit.type=='PARAM' and entit.param.mode=='CV':
                        TelFile.write('addi t0,sp,-%d\n' % (entit.param.offset))
                        TelFile.write('sw t0,-%d(fp)\n' % (12+4*i_s))
                     
                    elif entit.type=='PARAM' and entit.param.mode=='REF':
                        TelFile.write('lw t0,-%d(sp)\n' % (entit.param.offset))
                        TelFile.write('sw t0,-%d(fp)\n' % (12+4*i_s))
                   
                elif sco.nestingLevel<scopelist[-1].nestingLevel:#MONO sto perasma me anafora bazw thn gnlv kathws mono apo aftes tis sinthikes borw na exw mh topikh metavlhth
                    if entit.type=='PARAM' and entit.param.mode=='REF':
                        gnlvcode(totalQuads[i][2])
                        TelFile.write('lw t0,(t0)\n')
                        TelFile.write('sw t0,-%d(fp)\n' % (12+4*i_s))
                    else:
                         gnlvcode(totalQuads[i][2])
                         TelFile.write('sw t0,-%d(fp)\n' % (12+4*i_s))
                i_s=i_s+1
              
        elif(totalQuads[i][1] == 'call'):
            i_s=-1
            
            (sco,entit)=search_entity(totalQuads[i][2])
            if scopelist[-1].nestingLevel==entit.subprogram.nestingLevel:#an kalousa kai kleithisa exoun to idio bathmo fwliasmatos
                TelFile.write('lw t0,-4(sp)\n')
                TelFile.write('sw t0,-4(fp)\n')
            elif scopelist[-1].nestingLevel < entit.subprogram.nestingLevel:#an exoun diaforetiko bathmo fwliasmatos
                TelFile.write('sw sp,-4(fp)\n')
                
            TelFile.write('addi sp,sp,%d\n' % (entit.subprogram.frameLength))#ΠΑΝΤΑ μεταφερω δεικτη στοιβας στην κλειθησα
            TelFile.write('jal L%d\n' % (entit.subprogram.startQuad))
            TelFile.write('addi sp,sp,-%d\n' % (entit.subprogram.frameLength))#παιρνω πισω δεικτη στοιβας στην καλουσα
         
        elif(totalQuads[i][1] == 'begin_block' and scopelist[-1].nestingLevel!=0):#αν ξεκιναει υποπρογραμμα
            TelFile.write('sw ra,(sp)\n')
        
        elif(totalQuads[i][1] == 'begin_block' and scopelist[-1].nestingLevel==0):#αν ξεκιναει κυριο πρόγραμμα
            TelFile.seek(0, os.SEEK_SET)
            TelFile.write('j L%d\n'% (totalQuads[i][0]))
            TelFile.seek(0, os.SEEK_END)
            
            TelFile.write('addi sp,sp,%d\n' % (compute_offset()))
            TelFile.write('mv gp,sp\n')
        
        elif(totalQuads[i][1] == 'end_block' and scopelist[-1].nestingLevel!=0):#οταν τελειωνει υποπργραμμα
            TelFile.write('lw ra,(sp)\n')
            TelFile.write('jr ra\n')
          
        elif(totalQuads[i][1] == 'halt'):#οταν τελειωνει κυριο προγραμμα
            TelFile.write('li a0,0\n')
            TelFile.write('li a7,93\n')
            TelFile.write('ecall\n')
                
    totalQuads = []    
        
        
#arxi sintaktikou
def sintaktikos_analitis():#xrisimopoihoume thn grammatikh LL1 και φτιαχνουμε τον σωστο συντακτικο για την .gre γλωσσα
    global line
    global lexres #metavlhth lexres giana elegxei ta token kai na topothetei tis grammes twn token 
    
    
    def program():
        global line
        global lexres        
        if(lexres[0] == program_token):
            lexres = lex()
            line = lexres[2]           
            if(lexres[0]==id_token):
               myid = lexres[1] #dinw onoma sto προγραμμα
               lexres = lex()
               line = lexres[2]
               programblock(myid)
            else:
               print("error: Δεν δώθηκε όνομα στο πρόγραμμα",line)
               exit(0)
        else:
            print("error: Το αρχείο πρέπει να ξεκινάει με την λέξη 'πρόγραμμα'",line)
            exit(0)
           
           


    def programblock(name):
        global lexres 
        global line
        
        new_scope(name)#δημιουργει καινουργιο scope καθως ξεκιναει προγραμμα
        
        declarations()
        subprograms() 

        if(lexres[0]==start_program_token):
            lexres = lex()
            line = lexres[2]
            genquad('begin_block',name,'_','_')
            sequence()
            genquad('halt','_','_','_')
            genquad('end_block',name,'_','_')
            
            print_SYMPOL_TABLE()
            
            Telikos()
            
            delete_scope()
            
            if(lexres[0]==end_program_token):
               lexres = lex()
               line = lexres[2]
               
            else:
              print("error: Δεν υπάρχει η λέξη 'τέλος_προγράμματος' στο τέλος",line)
              exit(0)
        else:
            print("error: Δεν υπάρχει η λεξη 'αρχή_προγράμματος' στην αρχή",line)
            exit(0)
            
    
    
    def declarations():
        global lexres
         
        while(lexres[0]==decleration_token):
            lexres = lex()
            line = lexres[2]
            varlist(1)
            
            
            
    def varlist(flag):
        global lexres
        global line
        if(lexres[0]==id_token):
            myid = lexres[1]
            lexres = lex()
            line = lexres[2]
            
            if(flag == 1):
                ent = Entity()
                ent.type = 'VAR'
                ent.name = myid
                ent.var.offset = compute_offset()
                new_entity(ent)
            elif(flag == 2):
                arg = Argument()
                arg.name = myid
                arg.parMode = ''
                new_argument(arg)
            elif(flag == 3):
                for arg in scopelist[-1].entityList[-1].subprogram.argumentList:
                    if(arg.name == myid):
                        arg.parMode = 'CV'
            elif(flag == 4):
                for arg in scopelist[-1].entityList[-1].subprogram.argumentList:
                    if(arg.name == myid):
                        arg.parMode = 'REF'
                 
          
            while(lexres[0] == comma_token):
                lexres = lex()
                line = lexres[2]
                if(lexres[0]==id_token):
                    myid = lexres[1] 
                    lexres = lex()
                    line = lexres[2]
                   
                   
                    if(flag == 1):
                       ent = Entity()
                       ent.type = 'VAR'
                       ent.name = myid
                       ent.var.offset = compute_offset()
                       new_entity(ent)
                    elif(flag == 2):
                        arg = Argument()
                        arg.name = myid
                        arg.parMode = ''
                        new_argument(arg)
                    elif(flag == 3):
                        for arg in scopelist[-1].entityList[-1].subprogram.argumentList:
                            if(arg.name == myid):
                                arg.parMode = 'CV'
                    elif(flag == 4):
                        for arg in scopelist[-1].entity[-1].subprogram.argumentList:
                            if(arg.name == myid):
                                arg.parMode = 'REF'
                        
                else:
                   print("error: Δεν βρίσκω id μετα το ',' ",line)
                   exit(0)  
        
        else:
            print("error: Δεν υπάρχει id στη δήλωση",line)
            exit(0)           
                  
        
          
             
    def subprograms():
       global lexres
       
       while(lexres[0] == function_token or lexres[0] == procedure_token):
            if(lexres[0] == function_token):
                func()
            else:
                proc()
                    
    def func():
        global lexres
        global line
        if(lexres[0] == function_token):
            lexres = lex()
            line = lexres[2]
            if(lexres[0]==id_token):
                myid = lexres[1]
                lexres = lex()
                line = lexres[2]
                if(lexres[0] == left_parenth_token):
                    lexres = lex()
                    line = lexres[2]
                    
                    ent = Entity()
                    ent.type = 'SUBPR'
                    ent.name = myid
                    ent.subprogram.type = 'Function'
                    new_entity(ent)
                    
                    formalparlist()     
                    if(lexres[0] == right_parenth_token):
                       lexres = lex()
                       line = lexres[2]
                       funcblock(myid)
                    else:
                       print("error: Λείπει η δεξιά παρένθεση",line)
                       exit(0)
                else:
                   print("error: Λείπει η αριστερή παρένθεση",line)
                   exit(0)
            else:
               print("error: Δεν υπάρχει id μετα τo 'συνάρτηση'", line)
               exit(0)
    
    
    def proc():
        global lexres
        global line
        if(lexres[0]==procedure_token):
            lexres=lex()
            line=lexres[2]          
            if(lexres[0]==id_token):
                myid = lexres[1]
                lexres = lex()
                line = lexres[2]
                if(lexres[0] == left_parenth_token):
                    lexres = lex()
                    line = lexres[2]
                    
                    ent = Entity()
                    ent.type = 'SUBPR'
                    ent.name = myid
                    ent.subprogram.type = 'Procedure'
                    new_entity(ent)
                    
                    formalparlist()
                    if(lexres[0] == right_parenth_token):
                       lexres = lex()
                       line = lexres[2]
                       procblock(myid)
                    else:
                        print("ERROR: Λείπει η δεξιά παρένθεση",line)
                        exit(0)
                else:
                  print("error: Λείπει η αριστερή παρενθεση",line)
                  exit(0)
            else:
               print("error: Δεν υπάρχει id μετα το 'διαδικασία' ", line)
               exit(0)
                 
                 
    
    
    def formalparlist():
        global lexres
        if(lexres[0] == id_token):
           varlist(2)
          
          
          
          
    def funcblock(name):#για αρχη/τελος συναρτησησς
        global lexres
        global line
        if(lexres[0] == interface_token):
            lexres = lex()
            line = lexres[2]
            funcinput()
            funcoutput()
            
            new_scope(name)
            add_parameters()
            
            declarations()
            subprograms()
            if(lexres[0] == start_function_token):
                lexres = lex()
                line = lexres[2]
                
                compute_startQuad()
                genquad('begin_block',name,'_','_')
                sequence()
                compute_frameLength()
                genquad('end_block',name,'_','_')
                
                print_SYMPOL_TABLE()
                
                Telikos()
                
                delete_scope()
                
                if(lexres[0] == end_function_token):
                  lexres = lex()
                  line = lexres[2]                           
                else:
                  print("error: Λείπει στο τέλος η έκφραση 'τέλος_συνάρτησης'",line)
                  exit(0)
            else:
                print("error: Λείπει στην αρχή η έκφραση 'αρχή_συνάρτησης'",line)
                exit(0)
        else:
           print("error: Λείπει η λέξη 'διαπροσωπεία'",line)
           exit(0)
          
          
          
          
          
          
    def procblock(name):#για αρχη/τελος διαδικασιας 
        global lexres
        global line
        if(lexres[0] == interface_token):
            lexres = lex()
            line = lexres[2]
            funcinput()
            funcoutput()
            
            new_scope(name)
            add_parameters()
            
            declarations()
            subprograms()
            if(lexres[0] == start_procedure_token):
                lexres = lex()
                line = lexres[2]
                
                compute_startQuad()
                genquad('begin_block',name,'_','_')
                sequence()
                compute_frameLength()
                genquad('end_block',name,'_','_')
                
                print_SYMPOL_TABLE()
                
                Telikos()
                
                delete_scope()
                
                if(lexres[0] == end_procedure_token):
                  lexres = lex()
                  line = lexres[2]           
                else:
                   print("error: Λείπει στο τέλος η έκφραση 'τέλος_διαδικασίαs'",line)
                   exit(0)
            else:
               print("error: Λείπει στην αρχή η έκφραση 'αρχή_διαδικασίας'",line)
               exit(0)
        else:
           print("error: Λείπει στην αρχή η λέξη 'διαπροσωπεία'",line)
           exit(0)    


              
          
          
    
    def funcinput():
        global lexres
        if(lexres[0] == in_token):
            lexres = lex()
            line = lexres[2]
            varlist(3)
      
    
    def funcoutput():
        global lexres
        if(lexres[0] == out_token):
          lexres = lex()
          line = lexres[2]
          varlist(4)



    def sequence():
        global lexres
        global line                
        statement()
        while(lexres[0] == questionmark_token):
            lexres = lex()
            line = lexres[2]                                   
            statement()
             
             
             
             
    def statement():
        global lexres        
        if(lexres[0]==id_token):
               assignment_stat()
        elif(lexres[0]==if_token):
               if_stat()
        elif(lexres[0]==while_token):
               while_stat()
        elif(lexres[0]==repeat_token):
                do_stat()
        elif(lexres[0]==for_token):
                for_stat()
        elif(lexres[0]==read_token ):
                input_stat()
        elif(lexres[0]==wright_token):
                print_stat()
        elif(lexres[0]==execute_token):
                call_stat()
        else:
            print("error: Δεν βρέθηκε η εντολή",line)
            exit(0)
            
            
            
    def assignment_stat():
        global lexres
        global line                
        if(lexres[0] == id_token):
            ident = lexres[1] #ident einai h metavlhth
            lexres = lex()
            line = lexres[2]              
            if(lexres[0] == anathesi_token):
               lexres = lex()
               line = lexres[2]                               
               E_place = expression()
               genquad(':=', E_place, '_', ident) 
            else:
               print("error: Λείπει το σύμβολο ανάθεσης μετά την μεταβλητή",line)
               exit(0)




    def if_stat():
        global lexres
        global line               
        if(lexres[0] == if_token):
            lexres= lex()
            line = lexres[2]
            C = condition()#to kana wste na exw C[0]=cond.True kai C[1] = cond.False
            backpatch(C[0], nextquad())#an einai true ektelei to condition
            if(lexres[0]== then_token):
                lexres = lex()
                line = lexres[2]
                sequence()
                
                ifList = makelist(nextquad())
                genquad('jump', '_', '_', '_')
                backpatch(C[1], nextquad())#an einai false ektelei to else
                
                elsepart()
                
                backpatch(ifList, nextquad())
                if(lexres[0] == endif_token):
                   lexres= lex()
                   line = lexres[2]                                        
                else:
                   print("error: Λείπει η έκφραση 'εάν_τέλος' ", line)
                   exit(0)
            else:
              print("error: Λείπει η έκφραση 'τότε' ", line)
              exit(0)



    
    def elsepart():
        global lexres
        global line                
        if(lexres[0] == else_token):
          lexres = lex()
          line = lexres[2]
          sequence()
          
          
          
          
    def while_stat():
        global lexres
        global line                
        if(lexres[0]== while_token):
            lexres = lex()
            line = lexres[2]
           
            Bquad = nextquad()#wste na epistrepsei ekei otan kanei loupa
            C = condition()
            backpatch(C[0], nextquad())#an eiani true ektelei to sequance
           
            if(lexres[0] == repeat_token):
                lexres = lex()
                line = lexres[2]
                
                sequence()
                
                genquad('jump', '_', '_', Bquad)
                backpatch(C[1], nextquad())#an einai false paei exw apthn domh
              
                if(lexres[0] == endwhile_token):
                   lexres= lex()
                   line = lexres[2]
                else:
                   print("error: Λείπει η έκφραση 'όσο_τέλος' ", line)
                   exit(0)
            else:
               print("error: Λείπει η έκφραση 'επανάλαβε' ", line)
               exit(0)
              


    
    def do_stat():
        global lexres
        global line         
        if(lexres[0] == repeat_token):
            lexres = lex()
            line = lexres[2]
           
            Bquad = nextquad()
            sequence()
           
            if(lexres[0] == until_token):
               lexres = lex()
               line = lexres[2]
               C = condition()
               
               backpatch(C[1], Bquad)
               backpatch(C[0], nextquad())
            else:
               print("error: Λείπει η έκφραση 'μέχρι' ", line)
               exit(0)
              

    def for_stat():
        global lexres
        global line                
        if(lexres[0] == for_token):
            lexres = lex()
            line = lexres[2]                            
            if(lexres[0] == id_token):
                ident = lexres[1]
                lexres = lex()
                line = lexres[2]
                if(lexres[0] == anathesi_token):
                    lexres = lex()
                    line = lexres[2]
                    E1_place = expression()
                    genquad(':=', E1_place, '_', ident) 
                    if(lexres[0] == to_token):
                        lexres = lex()
                        line = lexres[2]
                        E2_place = expression()
                        stp = step()
                        Fquad = nextquad()
                        
                        ifStpPos = makelist(nextquad())
                        genquad('>', stp, '0', '_')
                        ifStpNeg = makelist(nextquad())
                        genquad('<', stp, '0', '_')
                        ifStpZero = makelist(nextquad())
                        genquad('=', stp, '0', '_')
                        
                        backpatch(ifStpPos, nextquad())
                        CheckLeavePos = makelist(nextquad())
                        genquad('>=', ident, E2_place, '_')
                        CheckStayPos = makelist(nextquad())
                        genquad('jump', '_', '_', '_')
                        
                        backpatch(ifStpNeg, nextquad())
                        CheckLeaveNeg = makelist(nextquad())
                        genquad('<=', ident, E2_place, '_')
                        CheckStayNeg = makelist(nextquad())
                        genquad('jump', '_', '_', '_')
                        
                        backpatch(ifStpZero, nextquad())  #epeidi an stp=0 tote atermonos vroxos
                        
                        if(lexres[0] == repeat_token):
                            lexres = lex()
                            line = lexres[2]
                            
                            backpatch(CheckStayPos, nextquad())
                            backpatch(CheckStayNeg, nextquad())
                            sequence()
                            
                            genquad('+', ident, stp, ident)
                            genquad('jump', '_', '_', Fquad)
                            
                            backpatch(CheckLeavePos, nextquad())
                            backpatch(CheckLeaveNeg, nextquad())
                            if(lexres[0] == endfor_token):
                               lexres = lex()
                               line = lexres[2]
                            else:
                               print("error: Λείπει η έκφραση 'για_τέλος' ", line)
                               exit(0)
                        else:
                           print("error: Λείπει η έκφραση 'επανάλαβε' ", line)
                           exit(0)
                    else:
                        print("error: Λείπει η έκφραση 'έως' ", line)
                        exit(0)
                else:
                    print("error: Λείπει το ':=' ", line)
                    exit(0)
            else:
                print("error: Δεν βρέθηκε id ", line)
                exit(0)
            
            
            
    
    def step():
        global lexres
        global line        
        if(lexres[0] == step_token):
           lexres = lex()
           line = lexres[2]
           E3_place = expression()
           return E3_place
        else:
              return '1'
           
           
           
           
    def print_stat():
        global lexres
        global line              
        if(lexres[0] == wright_token):
            lexres = lex()
            line = lexres[2]           
            E_place = expression()
            genquad('out', E_place, '_', '_') 


    def input_stat():
        global lexres
        global line         
        if(lexres[0] == read_token):#san to System.in
            lexres = lex()
            line = lexres[2]
            if(lexres[0] == id_token):
             ident = lexres[1]  
             lexres = lex()
             line = lexres[2]
             genquad('inp', ident, '_', '_')
            else:
              print("error: Δεν βρέθηκε id ", line)
              exit(0)  


    def call_stat():
        global lexres
        global line         
        if(lexres[0] == execute_token):
            lexres = lex()
            line = lexres[2]                      
            if(lexres[0] == id_token):
               id_n = lexres[1]
               
               lexres = lex()
               line = lexres[2]
               
               idtail(id_n, 1)#kathws ektelei diadikasia giafto exw caller = 1
               genquad('call', id_n, '_', '_')
            else:
               print("error: Δεν βρέθηκε id ", line)
               exit(0)              
             
             
             
    def idtail(name, caller):         #caller=1 procedure  caller=2 function
        global lexres
        global line                
        if(lexres[0] == left_parenth_token ):
            actualpars()
           
            if(caller == 2):#an einai sinartisi
                w=newtemp()#dhmiourgw kainourgia proswrinh metalbhth
                genquad('par', w, 'RET', '_')
                genquad('call', name, '_', '_')
                return w
        else:
            return name  #an einai metavliti


    def actualpars():
        global lexres
        global line         
        if(lexres[0] == left_parenth_token):
            lexres = lex()
            line = lexres[2]
            actualparlist()              
            if(lexres[0]==right_parenth_token):
               lexres = lex()
               line = lexres[2]
            else:
               print("error: Λείπει η δεξιά παρένθεση",line)
               exit(0)
              
              
    

    def actualparlist():
        global lexres
        global line         
        actualparitem()        
        while(lexres[0] == comma_token):
            lexres  = lex()
            line = lexres[2]            
            actualparitem()
    
          
          
    def actualparitem():#EDW EXETAZW AN H METABLHTH EXEI PERASTEI
        global lexres   #ME ANAFORA H ME TIMH
        global line
        if(lexres[0] == mod_token):
            lexres = lex()
            line = lexres[2]             
            if(lexres[0] == id_token):
               name = lexres[1]
               
               lexres = lex()
               line = lexres[2]
               
               genquad('par', name, 'REF', '_')
            else:
              print("error: Λείπει μεταβλητή μετά το '%' ", line)
              exit(0)
        else:
            Expression = expression()
            genquad('par', Expression, 'CV', '_')
            
            
    def condition():#epistrefei cond.true kai cond.false
        global lexres
        global line         
        B_T1 = boolterm()
        Cond_true = B_T1[0]
        Cond_false = B_T1[1]
        while(lexres[0]==or_token):
           lexres=lex()
           line = lexres[2]  
           backpatch(Cond_false, nextquad())
           
           B_T2 = boolterm()
           Cond_true = merge(Cond_true, B_T2[0])
           Cond_false = B_T2[1]
        return Cond_true, Cond_false   
           
           
           
           
    def boolterm():
        global lexres
        global line                
        B_F1 = boolfactor()
        B_True = B_F1[0]
        B_False = B_F1[1]
        while(lexres[0]==and_token):
            lexres=lex()
            line = lexres[2]
            backpatch(B_True, nextquad())
            B_F2 = boolfactor()
            
            B_False = merge(B_False, B_F2[1])
            B_True = B_F2[0]
        return B_True, B_False    
            
            
            
    def boolfactor():
        global lexres
        global line
        if(lexres[0]==not_token):
            lexres=lex()
            line = lexres[2]              
            if(lexres[0]==left_aggili_token):
                lexres = lex()
                line = lexres[2]                  
                C = condition()
                BF_true = C[1]
                BF_false = C[0]
                if(lexres[0]==right_aggili_token):
                    lexres = lex()
                    line = lexres[2]                       
                else:
                    print("error: Λείπει η δεξιά αγκύλη ",line)
                    exit(0)
            else:
                print("error: Λείπει η αριστερή αγκύλη", line)
                exit(0)
        elif(lexres[0]==left_aggili_token):
            lexres = lex()
            line = lexres[2]             
            C = condition()
            BF_true = C[0]
            BF_false = C[1]
            if(lexres[0]==right_aggili_token):
                lexres = lex()
                line = lexres[2]                                              
            else:
                print("error: Λείπει η δεξιά αγκύλη", line)
                exit(0)
        else:                 
            E1_place = expression()             
            relop = relational_oper()             
            E2_place = expression()
            
            BF_true=makelist(nextquad())
            genquad(relop, E1_place, E2_place, '_')
            BF_false=makelist(nextquad())
            genquad('jump', '_', '_', '_')
           
           
        return BF_true, BF_false   
           
           
    def expression():#epistrefei mia proswrinh metavlhth pou periexei mia ekfrash(πχ χ = χ + 2)
        global lexres              #########
        global line   
       
        opts = optional_sign()
       
        T1_place = term()
        
        if(opts == '-'):
            w = newtemp()
            genquad('-', '0', T1_place, w)
            T1_place = w
        
        while(lexres[0]==plus_token or lexres[0]==minus_token):
             plus_minus = add_oper()    
            
             T2_place = term()
            
            
             w = newtemp()
             genquad(plus_minus, T1_place, T2_place, w)
             T1_place = w
            
        E_place = T1_place
        return E_place
            
    
       
        
    def term():                   ######
        global lexres
        global line          
        F1_place = factor()          
        while(lexres[0]==multi_token or lexres[0]==divide_token):
            multi_div = mul_oper()
            F2_place = factor()
            
            w = newtemp()
            genquad(multi_div, F1_place, F2_place, w)
            F1_place = w
            
        T_place = F1_place
        return T_place
  
  
  
    def factor():
        global lexres
        global line               #####
        if(lexres[0]==number_token):
            Fact = lexres[1]
            
            lexres = lex()
            line = lexres[2]
        elif(lexres[0]==left_parenth_token):
            lexres = lex()
            line = lexres[2]
            E_place = expression()
            Fact = E_place
            if(lexres[0]==right_parenth_token):
                    lexres = lex()
                    line = lexres[2]                            
            else:
                print("error: Λείπει η δεξιά παρένθεση ",line)
                exit(0)
        elif(lexres[0]==id_token):
            temp_Fact = lexres[1]
            lexres = lex()
            line = lexres[2]
            Fact = idtail(temp_Fact, 2)    ####
        else:
          print("error: Δεν βρίσκω constant ή expression ή variable ",line)
          exit(0)
        
        return Fact
        
        
        
    def relational_oper():
        global lexres 
        global line
        if(lexres[0]==equal_token):  
            relop = lexres[1]
            lexres = lex()
            line = lexres[2]
        elif(lexres[0]==lessthan_token):
             relop = lexres[1]
             lexres = lex()
             line = lexres[2]
        elif(lexres[0]==lessORequal_token):
             relop = lexres[1]
             lexres = lex()
             line = lexres[2]
        elif(lexres[0]==diaforo_token):
             relop = lexres[1]
             lexres = lex()
             line = lexres[2]
        elif(lexres[0]== greaterthan_token):
             relop = lexres[1]
             lexres = lex()
             line = lexres[2]
        elif(lexres[0]==greaterORequal_token):
             relop = lexres[1]
             lexres = lex()
             line = lexres[2]
        else:
           print("error: ΛΕΙΠΕΙ '=' ή '<' ή '<=' ή '<>' ή '>=' ή '>' ",line)
           exit(0)
          
          
          
        return relop  
          
    def add_oper():
        global lexres 
        global line          
        if(lexres[0]==plus_token):            #####
           add_Oper = lexres[1]
           lexres = lex()
           line = lexres[2]
        elif(lexres[0]==minus_token):
            add_Oper = lexres[1]
            lexres = lex()
            line = lexres[2]
        return add_Oper  
          
          
    def mul_oper():
        global lexres 
        global line          
        if (lexres[0] == multi_token):
           operation = lexres[1]
           lexres = lex()                     #####
           line = lexres[2]
        elif (lexres[0] == divide_token):
              operation = lexres[1]
              lexres = lex()
              line = lexres[2]
              
        return operation      
   


    def optional_sign():
        global lexres                      #####
        global line
        if(lexres[0] == plus_token or lexres[0] == minus_token):
            addop = add_oper()
            return addop
        else:
            return '+'
            
            
    lexres= lex()
    line = lexres[2]
    program()
    


def WriteQuads(p):
     for quad in totalQuadsTeliko:
            line = str(quad[0]) + " : " + " , ".join([str(x) for x in quad[1:]]) + "\n"
            p.write(line)
    

    
    
    
    
    
File = open('intFile.int', 'w')
symFile = open('symFile.sy', 'w')
    
sintaktikos_analitis()
print("NO ERRORS WERE DETECTED")

WriteQuads(File)#kalw thn sinartisi gia to arxeio pouxei tis 4ades tou endiamesou
                #giana tis metatrepsw se asembly edoles
symFile.close()
File.close()
TelFile.close()