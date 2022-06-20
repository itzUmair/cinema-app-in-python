class login_signup:
    is_user = False
    user_name = ''

    is_admin = False
    admin_name = ''

    def __init__(self):
        self.checkLogin()

    def checkLogin(self):
        print('='*15 + ' GRANPLEX CINEMA ' + '='*15)
        choice = int(input('1.Admin Login\n2.User Login\n0.Exit\n'))
        if choice == 1:
            self.admin()
        
        if choice == 2:
            self.user()

        if choice == 0:
            print('='*50)
            print('\tThankyou for using our services')
            print('='*50)
            exit()
    
    def user(self):
        print('='*15 + ' USER LOGIN ' + '='*15)
        choice = int(input('1.login\n2.register\n0.exit\n'))
        if choice == 0:
            self.checkLogin()
        
        if choice == 1:
            userFound = False
            user_name = input('Enter your name: ')
            user_password = input('Enter your password: ')
            for x in open('database.txt', 'r').readlines():
                info = x.split()
                if user_name == info[0] and user_password == info[1]:
                    userFound = True
                    self.is_user = True
                    self.user_name = info[0]

            if not userFound:
                print("No users by these credentials were found! Try registering if you haven't registered yet.")
                self.user()
                self.is_user = False
        
        if choice == 2:
            user_name = input('Enter your name: ')
            user_password = input('Enter your password: ')
            file = open("database.txt","a")
            file.write(user_name)
            file.write(" ")
            file.write(user_password)
            file.write("\n")
            file.close()

            print('Registration done successfully! Try logging in.')
            self.user()

    def admin(self):
        admins = {'umair' : '123456', 'ali' : '123456', 'sufyan' : '123456', 'areeb' : '123456'}
        print('='*15 + ' ADMIN LOGIN ' + '='*15)
        choice = int(input('1.login\n0.exit\n'))
        if choice == 0:
            self.checkLogin()
        
        if choice == 1:
            userFound = False
            employee_name = input('Enter your name: ')
            employee_password = input('Enter your password: ')

            for x,y in admins.items():
                if employee_name == x and employee_password == y:
                    userFound = True
                    self.is_admin = True
                    self.admin_name = x

            if userFound == 0:
                print('No users by these credentials were found!')
                self.admin()
                self.is_admin = False

class Available_shows:
    def __init__(self):
        Available_shows.display_shows()

    shows = {
        'Jurassic world: Dominion' : {
            'Description' : "Four years after the destruction of Isla Nublar, dinosaurs now live--and hunt--alongside humans all over the world. This fragile balance will reshape the future and determine, once and for all, whether human beings are to remain the apex predators on a planet they now share with history's most fearsome creatures in a new Era." ,
            "Genre" : "Action , SCI-FI, Adventure" ,
            "Meta Score" : "37" , 
            "Seat Price" : "700" , 
            "Duration" : "2h 26m" ,
            "Actors" : "Chris Pratt, Bryce Dallas Howard, Laura Dern" ,
            "Time Slot 1" : "7:00 PM" ,
            "Time Slot 2" : "3:00 PM"
        },
        "Top Gun: Maverick" : {
            "Description" : "After more than thirty years of service as one of the Navy's top aviators, Pete Mitchell is where he belongs, pushing the envelope as a courageous test pilot and dodging the advancement in rank that would ground him." ,
            "Genre" : "Action, Drama" , 
            "Meta Score" : "78" , 
            "Seat Price" : "600" ,
            "Duration" : "2h 10m" ,
            "Actors" : "Tom Cruise, Jennifer Connelly, Miles Teller" ,
            "Time Slot 1" : "9:00 PM" ,
            "Time Slot 2" : "1:00 PM"
        },
        "Doctor Strange: Multiverse Of Madness" : {
            "Description" : "Doctor Strange teams up with a mysterious teenage girl from his dreams who can travel across multiverses, to battle multiple threats, including other-universe versions of himself, which threaten to wipe out millions across the multiverse. They seek help from Wanda the Scarlet Witch, Wong and others." , 
            "Genre" : "Action, Adventure, Fantasy" , 
            "Meta Score" : "60" , 
            "Seat Price" : "800" , 
            "Duration" : "2h 6m" ,
            "Actors" : "Benedict Cumberbatch, Elizebeth Olsen, Chiwetel Ejiofor" ,
            "Time Slot 1" : "5:00 PM" ,
            "Time Slot 2" : "4:00 PM"
        }
    }

    movie_titles = ['Jurassic world: Dominion', "Top Gun: Maverick", "Doctor Strange: Multiverse Of Madness"]

    booking = []


    def display_shows(self):
        count = 1
        print("We currently streaming the following shows: ")
        for x in Available_shows.shows.keys():
            print(count, x)
            count += 1
        Available_shows.user_choice(self)

    def user_choice(self):
        choice = int(input("Would you like to book a show?\n"))
        print("\n\nMovie name:" , Available_shows.movie_titles[choice-1],"\n\nDescription:" , Available_shows.shows[Available_shows.movie_titles[choice-1]]['Description'],"\n\nGenre:", Available_shows.shows[Available_shows.movie_titles[choice-1]]['Genre'], "\n\nMeta Score:", Available_shows.shows[Available_shows.movie_titles[choice-1]]['Meta Score'], "\n\nSeat Price:", Available_shows.shows[Available_shows.movie_titles[choice-1]]['Seat Price'], "\n\nDuration:", Available_shows.shows[Available_shows.movie_titles[choice-1]]['Duration'], "\n\nActors:", Available_shows.shows[Available_shows.movie_titles[choice-1]]['Actors'])

        choice2 = int(input("Book Seat?\n\n1.YES\n2.NO\n"))

        if choice2 == 1:
            print("Time Slots Available\n\n1:", Available_shows.shows[Available_shows.movie_titles[choice-1]]['Time Slot 1'], "\n2:", Available_shows.shows[Available_shows.movie_titles[choice-1]]['Time Slot 2'], "\n\n0. Go Back\n")
            choice3 = int(input("Which time slot do you prefer?\n"))
            
            Available_shows.booking.append(Available_shows.movie_titles[choice-1])

            if choice3 == 1:
                Available_shows.booking.append(Available_shows.shows[Available_shows.movie_titles[choice-1]]['Time Slot 1'])
            if choice3 == 2:
                Available_shows.booking.append(Available_shows.shows[Available_shows.movie_titles[choice-1]]['Time Slot 2'])
            if choice3 == 0:
                Available_shows.display_shows(self)

            print("Your seat has been booked for: ")
            for data in Available_shows.booking:
                print(data)

            cinema.change_seats(self)
            userDashboard.displayProfile(self)

        if choice2 == 2:
            Available_shows.display_shows(self)


    def remove_shows(self):
            count = 1
            print("Current shows ")
            for x in Available_shows.shows.keys():
                print(count, x)
                count += 1
            Available_shows.admin_choice(self)

    def admin_choice(self):
        choice = int(input("What show would you like to remove?\n\nTo Exit, press 0\n"))
        if choice != 0:
            print("\n\nMovie name:" , Available_shows.movie_titles[choice-1],"\n\nDescription:" , Available_shows.shows[Available_shows.movie_titles[choice-1]]['Description'],"\n\nGenre:", Available_shows.shows[Available_shows.movie_titles[choice-1]]['Genre'], "\n\nMeta Score:", Available_shows.shows[Available_shows.movie_titles[choice-1]]['Meta Score'], "\n\nSeat Price:", Available_shows.shows[Available_shows.movie_titles[choice-1]]['Seat Price'], "\n\nDuration:", Available_shows.shows[Available_shows.movie_titles[choice-1]]['Duration'], "\n\nActors:", Available_shows.shows[Available_shows.movie_titles[choice-1]]['Actors'])

        else:
            adminDashboard.displayProfile(self)

        choice2 = int(input("Remove show?\n\n1.YES\n2.NO\n"))

        if choice2 == 1:
            if len(Available_shows.shows) > 1:
                Available_shows.shows.pop(Available_shows.movie_titles[choice-1])
                Available_shows.movie_titles.remove(Available_shows.movie_titles[choice-1])
                print("\n\nShow removed successfully!")
                Available_shows.remove_shows(self)
            else:
                print("Cannot remove all shows")
                Available_shows.remove_shows(self)

        if choice2 == 2:
            Available_shows.remove_shows(self) 

    def add_show(self):
        show_name = input("Show name: \n")
        show_description = input("Show Description: \n")
        show_genre = input("Show Genre: \n")
        show_metaScore = input("Show Meta Score: \n")
        show_seatPrice = input("Show Seat Price: \n")
        show_duration = input("Show Duration: \n")
        show_actor = input("Show Actor: \n")
        show_time_slot1 = input("Time slot 1: \n")
        show_time_slot2 = input("Time slot 2: \n")

        Available_shows.shows[show_name] = {}
        Available_shows.shows[show_name]["Description"] =show_description
        Available_shows.shows[show_name]["Genre"] = show_genre
        Available_shows.shows[show_name]["Meta Score"] = show_metaScore
        Available_shows.shows[show_name]["Seat Price"] = show_seatPrice
        Available_shows.shows[show_name]["Duration"] = show_duration
        Available_shows.shows[show_name]["Actors"] = show_actor
        Available_shows.shows[show_name]["Time Slot 1"] = show_time_slot1
        Available_shows.shows[show_name]["Time Slot 2"] = show_time_slot2

        Available_shows.movie_titles.append(show_name)

        print("Show added successfully!")

        adminDashboard.displayProfile(self)
    
    def edit_show(self):
        count = 1
        print("Current shows ")
        for x in Available_shows.shows.keys():
            print(count, x)
            count += 1
        
        choice = int(input("\nWhich show would you like to edit?\n\nTo Exit, press 0"))

        if choice != 0:
            choice2 = input("What will you like to edit?\n")
            Available_shows.shows[Available_shows.movie_titles[choice-1]][choice2] = input("=>")
            print("Changes made successfully!\n")
            adminDashboard.displayProfile(self)

class adminDashboard(login_signup):
    def displayProfile(self):
        print('\n')
        print('='*15 + '  ADMIN DASHBOARD  ' + '='*15)
        print(f'\n\nWelcome {self.admin_name}')
        choice = int(input('\nWhat would you like to do?\n1.Set shows\n2.Check reservations\n3.Remove Shows\n4.Edit Shows\n0.Exit\n'))
        if choice == 1:
            Available_shows.add_show(self)

        if choice == 2:
            cinema.display_hall(self)

        if choice == 3:
            Available_shows.remove_shows(self)

        if choice == 4:
            Available_shows.edit_show(self)
            
        if choice == 0:
            login_signup.admin(self)

class userDashboard(login_signup , Available_shows):
    reservations = 'You currently have no reservations.'

    def __init__(self):
        self.displayProfile(self)        

    def displayProfile(self):
        print('\n')
        print('='*15 + '  USER DASHBOARD  ' + '='*15)
        print(f'Welcome {self.user_name}')
        userDashboard.display_reservations(self)

        choice = int(input('\nWhat would you like to do?\n1.Make reservations\n2.Cancel reservations\n3.Check available shows\n0.Exit\n'))
        
        if choice == 0:
            login_signup.user(self)
        
        if choice == 1:
            userDashboard.make_reservations(self)

        if choice == 2:
            userDashboard.cancel_reservation(self)

        if choice == 3:
            Available_shows.display_shows(self)

    def display_reservations(self):
        if len(Available_shows.booking) == 0:
            print(userDashboard.reservations)
        else:
            print("You have following reservation: ")
            for x in Available_shows.booking:
                print(x)
    
    def make_reservations(self):
        Available_shows.display_shows(self)

    def cancel_reservation(self):
        Available_shows.booking = []        
        print("All reservations cancelled successfully!")
        userDashboard.displayProfile(self)

class cinema(Available_shows):
    cinema_halls = [["Top Gun: Maverik", 50] , ["Jurassic world: Dominion", 50] , ["Doctor Strange: Multiverse Of Madness", 50]]

    def __init__(self):
        cinema.display_hall(self)

    def display_hall(self):
        choice = int(input("\n1. Display hall 1\n2. Display hall 2\n3. Display hall 3\n"))
        print("Current movie and available seats are: " )
        for x in cinema.cinema_halls[choice-1]:
            print(x)
        adminDashboard.displayProfile(self)
    
    def change_seats(self):
        remove_seat = Available_shows.booking[0]
        for x in cinema.cinema_halls:
            if remove_seat in x[0]:
                x[1] -= 1


a = login_signup()
if a.is_admin:
    adminDashboard.displayProfile(a)

if a.is_user:
    userDashboard.displayProfile(a)
 