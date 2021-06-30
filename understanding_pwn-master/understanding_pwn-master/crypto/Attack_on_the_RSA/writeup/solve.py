from Crypto.Util.number import *
import math

N =  117187799739088816439178283594737774234847566105762779984533933562731634880449069981008043473924258316276336588420636439754839823424692938548114859404968593001003108015853561101242345343453470236654844738176842290902452819810429910031517608311944047417666631954645349836945407693207863255329835415592656256181
e1 =  3
e2 =  65537
c1 =  17661725593133910124991307339935963864570318303745855280260002175618762653428740904082696134059547908473857852275159019164079499107452671983422882553164679584696849112738650416433832768956613013794954050818017605301769587767581584872239769264039556637186677873431742520119229587277415284718963530399313631672
c2 =  104645960848534548834452729271375511700929201234045355715140809442845507473006402850229315646296108903951949396425533025675804159773163792186769365344851444802520693563325689130690890227021251599665673062540404894503052344111665207448969208302531216313292569124476646457164757124201691307367597881609059471962

def egcd(a, b):
    if a == 0:
        return (b, 0, 1)
    else:
        g, y, x = egcd(b % a, a)
        return (g, x - (b // a) * y, y)

def modinv(a, m):
    g, x, y = egcd(a, m)
    return x % m

def common_modulus_attack(c1, c2, e1, e2, N):
    s1 = modinv(e1, e2)
    s2 = (math.gcd(e1, e2) - e1 * s1) // e2
    tmp = modinv(c2, N)
    m1 = pow(c1, s1, N)
    m2 = pow(tmp, -s2, N)
    return (m1 * m2) % N

print(long_to_bytes(common_modulus_attack(c1, c2, e1, e2, N)))