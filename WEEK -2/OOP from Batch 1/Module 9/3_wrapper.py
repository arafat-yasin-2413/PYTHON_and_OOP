'''
Python er moddhe function hoitase first class object
karon er moddhe parameter hishebe j kono kichui pathano jay
even, ekta function keu onno function er moddhe parameter hisebe pathano jay
tai function k first class object bola hoy . object bolte eikhne normal jinish
bojhano hoise. kono class er object hishebe bojhano hoy nai



'''



def do_something(work):
    print("Work Start")
    # print(work)
    work()
    print("Work done")


def coding():
    print('I am learning python')

do_something(coding)