#NATIVES
from pingmultiplo import pingMultiplo
from pingsimples import pingSimple

print ("Select action")

print ("1-One Ping Consulter 2-Multiple Ping Consulter \n2-Start Server UDP  3-Connect UDP" )

select= int(input ("Select funcion: "))

if select == 1:
    pingSimple()
if select == 2:
    pingMultiplo()
if select == 3:
    import clienteTCP
if select ==4():
    import clienteUDP