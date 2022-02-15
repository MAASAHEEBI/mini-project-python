class Flower_shop:
    def __init__(self,ShopName):
        self.name=ShopName
        self.flowers={}
        

    def seller(self):
        print('\n      Wel-Come to\n',self.name)
        while True:
            select=int(input('\n1.add flowers\n2.See prize\n3.Exite\n Please select from the above option:' ))
            if select==1:
                qty=int(input('\nHow many types of flower taken: ' ))
                for i in range(1,qty+1):
                    flowers=input('\nEnter the name of the flowers: ')
                    self.flowers[i]=flowers
                return self.flowers

            elif select==2:
                 prize=10
                 T_Prize=prize*len(self.flowers)
                 print('\nTotal prize is: ')
                 return T_Prize

            elif select==3:
                return('\n!!thank u!!\n')
                break
            else:
                return('\n!!invalid option,please enter correct one!!\n')

    
            
        

    def costomer(self):
        print('      Wel-Come to\n',self.name)
        print('\ndo you want to book boque? \n1.yes \n2.no')
        choice=int(input('\nplease select above options:'))
        names=[]
        self.prize=10
        while True:
            if choice==1:
                qty=int(input('\nHow many types of cobination you want: '))
                for i in range(qty):
                    flower=input('\nplease enter the name of flowers boque you want:' )
                    names.append(flower)
                print(names)
                T_Prize=len(names)*self.prize
                print('Total prize is:')
                return T_Prize

                
            elif choice==2:
                 print('\n!!!Thank you for coming !!!\n')
                 break
            else:
                return('\ninvalid input. Try again.')
       
        

    def View_n_select(self):
            print('\nThese is the list of flowers available,\n Please select from this.')
        
            print('\nAvailable list of flowers are:')
            return self.flowers
    
            
        
            
F=Flower_shop('!!!Dil Garden Garden!!!\n')

while True:
            
    select=int(input('\nplease select the below option.\n1.Seller\n2.Costomer\n3.View n select folwers\n0.Exit\nEnter option: \n' ))
    if select==1:
        print(F.seller())
    elif select==2:
        print(F.costomer())
    elif select==3:
        print(F.View_n_select())
    else:
        print('\n!!!visit again!!!\n')
        break

    
    


    
