un = 0
def Main_menu():
        print("""
                1 ---> Jaipur                          
                2 ---> Agra                            
                3 ---> Mumbai                           
                4 ---> Goa                              
                5 ---> Udaipur                       
                6 ---> Varanasi                       
                7 ---> Bengaluru                       
                8 ---> Jodhpur
                5 ---> Udaipur
                9 ---> Manali                         
                10 ---> Shimla                        
                11 ---> Alappuzha                     
                12 ---> Chennai                       
                13 ---> Kochi                          
                14 ---> Fatehpur Sikri                
                15 ---> Darjelling                   
                16 ---> Kovalam                       
                17 ---> Rishikesh                    
                18 ---> Punducherry                    
                19 ---> Hampi                        
                20 ---> Khajuraho                     
                      """)
        h = int(input("Your Choce: "))
        if h == 1:
            Dest = "Jaipur"
        elif h == 2 :
            Dest = "Agra"
        elif h == 3 :
            Dest = "Mumbai"
        elif h == 4 :
            Dest = "Goa"
        elif h == 5 :
            Dest = "Udaipur"   
        elif h == 6 :
            Dest = "Varanasi"
        elif h == 7 :
            Dest = "Bengaluru"         
        elif h == 8 :
            Dest = "Jodhpur"      
        elif h == 9 :
            Dest = "Manali"          
        elif h == 10 :
            Dest = "Shimla"          
        elif h == 11 :
            Dest = "Alappuzha" 
        elif h == 12 :
            Dest = "Chennai"
        elif h == 13 :
            Dest = "Kochi"
        elif h == 14 :
            Dest = "Fatehpur Sikri"
        elif h == 15 :
            Dest = "Darjelling"
        elif h == 16 :
            Dest = "Kovalam"
        elif h == 17 :
            Dest = "Rishikesh"
        elif h == 18 :
            Dest = "Punducherry"
        elif h == 19 :
            Dest = "Hampi"
        elif h == 20 :
            Dest = "Khajuraho"
        else:
            print("Invalid Input")
        print()
        print()
        print()
        Dep = input("Please Enter the Departure Date (DD/MM/YYYY): ")
        print()
        print()
        print()
        rtn = input("Please Enter the Return Date (DD/MM/YYYY): ")
        print()
        print()
        print()
        print()
        print()
        print()
        print("Thank You for Choosing Us .")
        
        mycursor.execute("insert into travel_info(Name,Destination,Date_of_Departure,Date_of_return) values('"+un+"','"+Dest+"','"+Dep+"','"+rtn+"');")
        mysql.commit()
def login():
                        ## Printing the login form after Regestration (by calling fun)
                        print("""
                =================================================================================
                                                     Sign in 
                =================================================================================
                    """)
                        global un
                        un = input("Username: ")
                        ea = input("Email Address: ")
                        ps=input("Password: ")
                        mycursor.execute("select Password from user_data where username='"+un+"'")
                        row=mycursor.fetchall()
                        for i in row:
                            
                            a = list(i)
                        if a[0]==str(ps):
                            
                            print("""
                =================================================================================
                                              You Have Successfully Logged in
                =================================================================================
                    """)
                        else:
                            print("Invalid Password......")
def create_acc():
                        
                        
                    
                        print("""
                =================================================================================
                                               Create an account for yourself
                =================================================================================
                    """)
                        un = input("Username:* ")
                        e = input("Email Address:* ")
                        p = input("Password:(Min 8 Characters)* ")
                
                        ##Entering data into database
                
                        mycursor.execute("insert into user_data values('"+un+"','"+e+"','"+p+"')")
                        mysql.commit()
                        print("""
                =================================================================================
                                               You Have Successfully Registered
                =================================================================================
                    """)



##PRINTING THE WELCOME NOTE
while(True):
    print("""
                                        ............................................................................
                                        ////////////////////////////////////////////////////////////////////////////
                                        .................... WELCOME TO CENTRAL PERK TRAVELS .......................
                                        ////////////////////////////////////////////////////////////////////////////
                                        ............................................................................
                """)
    ###Creating database connectivity
    
    import mysql.connector
    passwd=str(input("Enter your Database Password: "))
    
    mysql=mysql.connector.connect(host="localhost",user="root",passwd=passwd)
    mycursor=mysql.cursor()
    
    ##Creating database
    while(True):
        mycursor.execute("create database if not exists Central_Perk")
        mycursor.execute("use Central_Perk")
        
        ##Creating the tables we need
        
        mycursor.execute("create table if not exists Clint_Info(Name varchar(20) not null,Phone_no int(10) not null, Email_id varchar(30) not null primary key, Address varchar(50) not null);")
        
        mycursor.execute("create table if not exists Travel_Info (Sno int not null primary key auto_increment,Name varchar(20) not null, Destination varchar(30) not null, Date_of_Departure varchar(30) not null, Date_of_return varchar(30) not null);")
        mycursor.execute("create table if not exists contact_us(Name varchar(20), email varchar(30), Mobile_number int(10), Package varchar(50));")
        ##Login or signup option
        ##Creating table for storing the username and password of the user
        mycursor.execute("create table if not exists user_data(Username varchar(10) not null,Email varchar(20) not null, Password varchar(30) default'123');")
  
        while(True):
            print("""
            1. Sign in (Login)
            2. Sign up (Register)
                """)
            r = int(input("Enter your choice: "))
            while(True):
                ## Registration Form
                if r == 1:
                    login()

                else:
                    create_acc()
                    
                x=input("Enter any key to continue:")
                
                ## Login Form
            
                while(True):
                    print("1---> New Bookings")
                    print("2---> Check Status Of existing Booking")
                    print("3---> Reschedule The Booking")
                    print("4---> Customer Care")
                    print("5---> Terms & Contitions")
                    print("6---> Cancel Booking")
                    print("7---> To Quit")
                    print()
                    print()
                    print()
                        
                    # asking users choice    
                
                    f = int(input("Enter Your choice: "))
                    
                    if f == 1:
                        print("Please Choose Where do You want to Travel: ")
                        print()
                        print()
                        print()
                        Main_menu()

                        # code for checking status
                    if f == 2 :
                        mycursor.execute("select * from travel_info where name = '"+un+"';")
                        for row in mycursor:
                            print(row)
                            print()

                    # Code to Reschedule  
                    if f == 3 :
                        print("Please choose that Sno.(Extreme Left) of that Booking----")
                        mycursor.execute("select * from travel_info where name = '"+un+"';")
                        print()
                        print()
                        for row in mycursor:
                            print(row)
                        print()
                        print()
                        l =(input("Your Choice: "))
                        mycursor.execute("Delete from Travel_info where sno = '"+l+"';")
                        print("Your Old Booking is deleted please create a new onee: ")
                        print()
                        print()
                        print()
                        Main_menu()
                        

                    # code for custemor care
                    if f == 4:
                         print("""
                    =================================================================================
                                                      Contact Form
                    =================================================================================
                         """)
                         u = input("Name: ")
                         y = input("Email ID: ")
                         o = input("Phone number: ")
                         m = input("Your Package: ")
                         mycursor.execute("insert into contact_us values('"+u+"','"+y+"','"+o+"','"+m+"')")
                         print()
                         print()
                         print()
                         print("Our Team will get in touch with you within 48hrs")
                         print()
                         print()
                         print()
                         
                        
                           
                
                    # code for terms and condition
                    if f == 5:
                        print("""                                            FIND BUS TICKET WITH CENTRAL PERK TRAVELS
                    Making the right travel arrangements is the genesis of any good holiday. Providing exceptional bus travel arrangements is the mantra that’s followed at Central perk travels. India’s largest online bus ticketing platform has driven the country’s bus booking journey over the past 13+ years through thousands of bus operators and routes. Striving to reach new heights when it comes to online bus booking in India, Central perk travels has become the right tool to use to have a smooth bus ticket booking experience. Anybody can use the official website of Central perk travels or the user-friendly app to book their bus tickets from anywhere in the country. From the comfort of your home or from or office or vehicle, you can now make an online bus booking with ease. With these successful USPs, Central perk travels have expanded internationally to countries like Singapore, Malaysia, Indonesia, Peru and Columbia.
                
                    Why book bus tickets through Central perk travels
                    The online bus booking services of Central perk travels offers a plethora of advantages than its offline prehistoric booking modes. Firstly, booking a bus ticket through a travel agent or at a counter is in the past. People have begun to recognize the advantages of making an online bus booking.
                
                    At a counter, people would have to first stand in a queue in front of a particular bus operator. Once they reach the counter, they would have to book a seat among the seats that are available. If a seat isn’t available on the bus of their choice, the dejected customer would then have to stand in another queue in front of another bus operator. Online bus ticket booking with Central perk travels has eliminated these problems that people used to face.
                
                    With Central perk travels, customers can view every bus that’s available on any given route in India. They do not have to stand in a queue and accept the price and seat that’s given to them by the travel agent or the ticket clerk behind the counter. Customers can view every detail of the bus including updated pictures of the bus, the type of bus, amenities offered, and much more on the Central perk travels website and app. Customers can even avail exclusive discounts while making their bus reservation which are offered by Central perk travels that cannot be matched by any discount offered by a travel agent or a counter.
                
                    M-ticket and its advantages
                    Have you ever gone to your boarding point and realized that you did not carry your ticket? That feeling can be terrible especially if it’s for a holiday that you’ve taken leaves or made special arrangements for. The M-ticket initiative by Central perk travels was a game-changer in countless ways. Not only did it put an end to the physical form of a ticket or a printout of a bus ticker but it also ensured that passengers didn’t have to rush back home in case they didn’t have their ticket.
                
                    Once a passenger completes their bus ticket booking procedure, Central perk travels will confirm that the booking has been made. The bus ticket is then sent to the customer’s registered mobile number in the form of an M-ticket and it’s also sent to the registered email ID of the customer. With Central perk travels’ advanced interface, this process takes a few milliseconds to complete.
                
                    Customers are advised to carry a government-approved identity card that can be used to prove their identity when they have to board their bus.
                
                    On-Time Guarantee with Central perk travels
                    Here's another reason why Central perk travels should be your one-stop destination when it comes to bus ticket booking. The On-Time Guarantee is a unique feature that’s offered by Central perk travels for the benefit of every customer. Look for the “On-Time Guarantee” tag that’s marked against a bus on the route you’ve searched for. If you book bus tickets for your family or yourself on a “On-Time Guarantee” tag, you or your family will fall under the benefits mentioned below:
                
                    •	Bus On Time: With this benefit, customers will receive a 25% refund on their bus ticket costs in case the bus that they need to travel in is delayed by 30 minutes.
                    •	No Bus Cancellation: If you made an online bus booking through Central perk travels and the bus operator cancels the bus without making any alternate arrangements, the customer will receive a 150% refund on their bus ticket costs.
                    •	Alternate Assurance: If a bus breaks down during the journey, the customers who are traveling on the bus would have to wait for an alternate arrangement to be made by the bus operator. If this arrangement is not made within 6 hours from the time of the breakdown, the customers will be eligible for a 300% refund on their bus tickets.
                
                    Payment Modes on Central perk travels
                    There are a plethora of payment modes that are available on the Central perk travels website and app. Choose a payment mode that meets your needs and complete the bus ticket booking process. Some of these payment modes that are available are:
                
                    •	Debit Card
                    •	Credit Card
                    •	Net Banking with banks like:
                    •	HDFC Bank
                    •	ICICI Bank
                    •	Indian Bank
                    •	Axis Bank
                    •	State Bank of India and many more
                    •	Google Pay
                    •	Amazon Pay where customers can earn Rs.10 to Rs.300 when they book bus tickets for a minimum of Rs.300 and this is applicable once per user when they use Amazon Pay during the offer period
                    •	PhonePe
                    •	UPI (Unified Payment Interface) where you will be asked to enter your VPA (Virtual Payment Address)
                    •	MobiKwik
                
                    Track my Bus
                    Have you ever reached your boarding point and wondered about the whereabouts of your bus? Have you ever had a heated conversation with the bus operator about the location of your bus? Central perk travels has addressed these worries and more with the “Track My Bus” feature. With this, customers can track their bus on their app to help them plan their journey to the boarding point or to get off at their desired drop-off point.
                
                    If the passenger has to be picked up from the drop-off point, they can always share the live location of the bus to help them plan their commute to the drop-off location. This feature also adds to improving the safety standards on the bus. Family members can breathe a sigh of relief as they can always keep a track of the location of the bus in which their loved ones are traveling in. Visit https://www.Central perk travels.in/info/track-my-bus and enter the ticket number and registered email ID to track the concerned bus.
                
                    How to book bus tickets online?
                    Booking a bus or making an online booking has never been this easy thanks to Central perk travels. After setting industry standards that other competitors have struggled to reach, Central perk travels have now raised the bar again by providing a bus booking experience like no other. Customers have to only follow these simple steps to make an online bus booking with Central perk travels:
                
        5        
                    """)
                        
                
                    #code for Cancel booking
                    if f == 6:
                        print("Please choose the Sno. of that Booking")
                        print()
                        print()
                        mycursor.execute("select * from travel_info where name = '"+un+"';")
                        for row in mycursor:
                            print(row)
                        print()
                        print()
                        q =(input("Your Choice (Sno.): "))
                        mycursor.execute("Delete from Travel_info where sno = '"+q+"';")
                        print("Hope to see you soon :)")
                        print()
                        print()
                        print()
                    
                
                    if f ==7:
                        exit()
                        
    break
