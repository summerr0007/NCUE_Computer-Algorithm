import math 
maxsize =float ('inf')
def cM (currp ):
    final_path [:N +1 ]=currp [:]
    final_path [N ]=currp [0 ]
def fM (a ,i ):
    mn =maxsize 
    for kk in range (N ):
        if a [i ][kk ]<mn and i !=kk :
            mn =a [i ][kk ] 
    return mn 
def sM (ad ,ii ):
    ft ,snd =maxsize ,maxsize 
    for j in range (N ):
        if ii ==j :
            continue 
        if ad [ii ][j ]<=ft :
            snd =ft 
            ft =ad [ii ][j ]
        elif (ad [ii ][j ]<=snd and ad [ii ][j ]!=ft ):
            snd =ad [ii ][j ]
    return snd 
def TSPR (dj ,cuund ,cw ,lv ,lpa ,vis ):
    global final_res 
    if lv ==N :
        if dj [lpa [lv -1 ]][lpa [0 ]]!=0 :
            crr =cw +dj [lpa [lv -1 ]][lpa [0 ]]
            if crr <final_res :
                cM (lpa )
                final_res=crr
        return 
    for i in range (N ):
        if (dj [lpa [lv -1 ]][i ]!=0 and vis [i ]==False ):
            t =cuund 
            cw +=dj [lpa [lv -1 ]][i ]
            if lv ==1 :
                cuund -=((fM (dj ,lpa [lv -1 ])+fM (dj ,i ))/2 )
            else :
                cuund -=((sM (dj ,lpa [lv -1 ])+fM (dj ,i ))/2 )
            if cuund +cw <final_res :
                lpa [lv ]=i 
                vis [i ]=True 
                TSPR (dj ,cuund ,cw ,lv +1 ,lpa ,vis )
            cw -=dj [lpa [lv -1 ]][i ]
            cuund =t 
            vis =[False ]*len (vis )
            for j in range (lv ):
                if lpa [j ]!=-1 :
                    vis [lpa [j ]]=True 
def TSP (aj ):
    cuund =0 
    lpa =[-1 ]*(N +1 )
    vis =[False ]*N 
    for i in range (N ):
        cuund +=(fM (aj ,i )+sM (aj ,i ))
    cuund =math .ceil (cuund /2 )
    vis [0 ]=True 
    lpa [0 ]=0 
    TSPR (aj ,cuund ,0 ,1 ,lpa ,vis )
f =open ("test.txt",'r')
text =f .read ()
f .close ()
list =text .split ()
N =int (list [0 ])
adj =[[0 for i in range (int (N ))]for j in range (int (N ))]
count =1 
for i in range (int (N )):
    for j in range (int (N )):
        adj [i ][j ]=int (list [count ])
        count =count +1 
final_path =[None ]*(N +1 )
visited =[False ]*N 
final_res =maxsize 
TSP (adj )
print ("Order of nodes : ",end =' ')
for i in range (N +1 ):
    print (final_path [i ],end =' ')
print ("\nMinimum cost :",final_res )
