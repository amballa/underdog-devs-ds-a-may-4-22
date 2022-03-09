# ---
# jupyter:
#   jupytext:
#     text_representation:
#       extension: .py
#       format_name: light
#       format_version: '1.5'
#       jupytext_version: 1.13.7
#   kernelspec:
#     display_name: Python 3
#     name: python3
# ---

# + [markdown] id="TQrXpzY7U9qF"
# #Mock Data
#
# There have been some models created already around some simplistic data sets, I want to create a more complex mock dataset to hopefully give a test model a run for its money. The data points are based off the intake survey, so if anyone has any suggestions on that, I'm all ears! ^_^ 
#
# I was thinking about using the following features for the model to consider:
#
# - skills 
# - mentee_load 
# - career_capable 
# - availability 
#
# All of the features of note for matching are housed within the Mentor Class. 
#
# Let me know if anyone else can think of any other relevant data points we should be using in our matching criteria. 

# + [markdown] id="ADc8o36PWDl0"
# ## Update
#
# After our latest Stakeholder meeting, we decided to clean up the mock data a little bit and remove some previous features and add some different ones. The mock data now has a more streamline approach for the model that will be coming. 

# + id="XqhBBraSFaO4"
# The following is basically source data, the real fun starts in the next code cell

male_first_name = (
    'Liam',
    'Noah',
    'Oliver',
    'Elijah',
    'William',
    'James',
    'Benjamin',
    'Lucas',
    'Henry',
    'Alexander',
    'Mason',
    'Michael',
    'Ethan',
    'Daniel',
    'Jacob',
    'Logan',
    'Jackson',
    'Levi',
    'Sebastian',
    'Mateo',
    'Jack',
    'Owen',
    'Theodore',
    'Aiden',
    'Samuel',
    'Joseph',
    'John',
    'David',
    'Wyatt',
    'Matthew',
    'Luke',
    'Asher',
    'Carter',
    'Julian',
    'Grayson',
    'Leo',
    'Jayden',
    'Gabriel',
    'Isaac',
    'Lincoln',
    'Anthony',
    'Hudson',
    'Dylan',
    'Ezra',
    'Thomas',
    'Charles',
    'Christopher',
    'Jaxon',
    'Maverick',
    'Josiah',
    'Isaiah',
    'Andrew',
    'Elias',
    'Joshua',
    'Nathan',
    'Caleb',
    'Ryan',
    'Adrian',
    'Miles',
    'Eli',
    'Nolan',
    'Christian',
    'Aaron',
    'Cameron',
    'Ezekiel',
    'Colton',
    'Luca',
    'Landon',
    'Hunter',
    'Jonathan',
    'Santiago',
    'Axel',
    'Easton',
    'Cooper',
    'Jeremiah',
    'Angel',
    'Roman',
    'Connor',
    'Jameson',
    'Robert',
    'Greyson',
    'Jordan',
    'Ian',
    'Carson',
    'Jaxson',
    'Leonardo',
    'Nicholas',
    'Dominic',
    'Austin',
    'Everett',
    'Brooks',
    'Xavier',
    'Kai',
    'Jose',
    'Parker',
    'Adam',
    'Jace',
    'Wesley',
    'Kayden',
    'Silas',
    'Bennett',
    'Declan',
    'Waylon',
    'Weston',
    'Evan',
    'Emmett',
    'Micah',
    'Ryder',
    'Beau',
    'Damian',
    'Brayden',
    'Gael',
    'Rowan',
    'Harrison',
    'Bryson',
    'Sawyer',
    'Amir',
    'Kingston',
    'Jason',
    'Giovanni',
    'Vincent',
    'Ayden',
    'Chase',
    'Myles',
    'Diego',
    'Nathaniel',
    'Legend',
    'Jonah',
    'River',
    'Tyler',
    'Cole',
    'Braxton',
    'George',
    'Milo',
    'Zachary',
    'Ashton',
    'Luis',
    'Jasper',
    'Kaiden',
    'Adriel',
    'Gavin',
    'Bentley',
    'Calvin',
    'Zion',
    'Juan',
    'Maxwell',
    'Max',
    'Ryker',
    'Carlos',
    'Emmanuel',
    'Jayce',
    'Lorenzo',
    'Ivan',
    'Jude',
    'August',
    'Kevin',
    'Malachi',
    'Elliott',
    'Rhett',
    'Archer',
    'Karter',
    'Arthur',
    'Luka',
    'Elliot',
    'Thiago',
    'Brandon',
    'Camden',
    'Justin',
    'Jesus',
    'Maddox',
    'King',
    'Theo',
    'Enzo',
    'Matteo',
    'Emiliano',
    'Dean',
    'Hayden',
    'Finn',
    'Brody',
    'Antonio',
    'Abel',
    'Alex',
    'Tristan',
    'Graham',
    'Zayden',
    'Judah',
    'Xander',
    'Miguel',
    'Atlas',
    'Messiah',
    'Barrett',
    'Tucker',
    'Timothy',
    'Alan',
    'Edward',
    'Leon',
    'Dawson',
    'Eric',
    'Ace',
    'Victor',
    'Abraham',
    'Nicolas',
    'Jesse',
    'Charlie',
    'Patrick',
    'Walker',
    'Joel',
    'Richard',
    'Beckett',
    'Blake',
    'Alejandro',
    'Avery',
    'Grant',
    'Peter',
    'Oscar',
    'Matias',
    'Amari',
    'Lukas',
    'Andres',
    'Arlo',
    'Colt',
    'Adonis',
    'Kyrie',
    'Steven',
    'Felix',
    'Preston',
    'Marcus',
    'Holden',
    'Emilio',
    'Remington',
    'Jeremy',
    'Kaleb',
    'Brantley',
    'Bryce',
    'Mark',
    'Knox',
    'Israel',
    'Phoenix',
    'Kobe',
    'Nash',
    'Griffin',
    'Caden',
    'Kenneth',
    'Kyler',
    'Hayes',
    'Jax',
    'Rafael',
    'Beckham',
    'Javier',
    'Maximus',
    'Simon',
    'Paul',
    'Omar',
    'Kaden',
    'Kash',
    'Lane',
    'Bryan',
    'Riley',
    'Zane',
    'Louis',
    'Aidan',
    'Paxton',
    'Maximiliano',
    'Karson',
    'Cash',
    'Cayden',
    'Emerson',
    'Tobias',
    'Ronan',
    'Brian',
    'Dallas',
    'Bradley',
    'Jorge',
    'Walter',
    'Josue',
    'Khalil',
    'Damien',
    'Jett',
    'Kairo',
    'Zander',
    'Andre',
    'Cohen',
    'Crew',
    'Hendrix',
    'Colin',
    'Chance',
    'Malakai',
    'Clayton',
    'Daxton',
    'Malcolm',
    'Lennox',
    'Martin',
    'Jaden',
    'Kayson',
    'Bodhi',
    'Francisco',
    'Cody',
    'Erick',
    'Kameron',
    'Atticus',
    'Dante',
    'Jensen',
    'Cruz',
    'Finley',
    'Brady',
    'Joaquin',
    'Anderson',
    'Gunner',
    'Muhammad',
    'Zayn',
    'Derek',
    'Raymond',
    'Kyle',
    'Angelo',
    'Reid',
    'Spencer',
    'Nico',
    'Jaylen',
    'Jake',
    'Prince',
    'Manuel',
    'Ali',
    'Gideon',
    'Stephen',
    'Ellis',
    'Orion',
    'Rylan',
    'Eduardo',
    'Mario',
    'Rory',
    'Cristian',
    'Odin',
    'Tanner',
    'Julius',
    'Callum',
    'Sean',
    'Kane',
    'Ricardo',
    'Travis',
    'Wade',
    'Warren',
    'Fernando',
    'Titus',
    'Leonel',
    'Edwin',
    'Cairo',
    'Corbin',
    'Dakota',
    'Ismael',
    'Colson',
    'Killian',
    'Major',
    'Tate',
    'Gianni',
    'Elian',
    'Remy',
    'Lawson',
    'Niko',
    'Nasir',
    'Kade',
    'Armani',
    'Ezequiel',
    'Marshall',
    'Hector',
    'Desmond',
    'Kason',
    'Garrett',
    'Jared',
    'Cyrus',
    'Russell',
    'Cesar',
    'Tyson',
    'Malik',
    'Donovan',
    'Jaxton',
    'Cade',
    'Romeo',
    'Nehemiah',
    'Sergio',
    'Iker',
    'Caiden',
    'Jay',
    'Pablo',
    'Devin',
    'Jeffrey',
    'Otto',
    'Kamari',
    'Ronin',
    'Johnny',
    'Clark',
    'Ari',
    'Marco',
    'Edgar',
    'Bowen',
    'Jaiden',
    'Grady',
    'Zayne',
    'Sullivan',
    'Jayceon',
    'Sterling',
    'Andy',
    'Conor',
    'Raiden',
    'Royal',
    'Royce',
    'Solomon',
    'Trevor',
    'Winston',
    'Emanuel',
    'Finnegan',
    'Pedro',
    'Luciano',
    'Harvey',
    'Franklin',
    'Noel',
    'Troy',
    'Princeton',
    'Johnathan',
    'Erik',
    'Fabian',
    'Oakley',
    'Rhys',
    'Porter',
    'Hugo',
    'Frank',
    'Damon',
    'Kendrick',
    'Mathias',
    'Milan',
    'Peyton',
    'Wilder',
    'Callan',
    'Gregory',
    'Seth',
    'Matthias',
    'Briggs',
    'Ibrahim',
    'Roberto',
    'Conner',
    'Quinn',
    'Kashton',
    'Sage',
    'Santino',
    'Kolton',
    'Alijah',
    'Dominick',
    'Zyaire',
    'Apollo',
    'Kylo',
    'Reed',
    'Philip',
    'Kian',
    'Shawn',
    'Kaison',
    'Leonidas',
    'Ayaan',
    'Lucca',
    'Memphis',
    'Ford',
    'Baylor',
    'Kyson',
    'Uriel',
    'Allen',
    'Collin',
    'Ruben',
    'Archie',
    'Dalton',
    'Esteban',
    'Adan',
    'Forrest',
    'Alonzo',
    'Isaias',
    'Leland',
    'Jase',
    'Dax',
    'Kasen',
    'Gage',
    'Kamden',
    'Marcos',
    'Jamison',
    'Francis',
    'Hank',
    'Alexis',
    'Tripp',
    'Frederick',
    'Jonas',
    'Stetson',
    'Cassius',
    'Izaiah',
    'Eden',
    'Maximilian',
    'Rocco',
    'Tatum',
    'Keegan',
    'Aziel',
    'Moses',
    'Bruce',
    'Lewis',
    'Braylen',
    'Omari',
    'Mack',
    'Augustus',
    'Enrique',
    'Armando',
    'Pierce',
    'Moises',
    'Asa',
    'Shane',
    'Emmitt',
    'Soren',
    'Dorian',
    'Keanu',
    'Zaiden',
    'Raphael',
    'Deacon',
    'Abdiel',
    'Kieran',
    'Phillip',
    'Ryland',
    'Zachariah',
    'Casey',
    'Zaire',
    'Albert',
    'Baker',
    'Corey',
    'Kylan',
    'Denver',
    'Gunnar',
    'Jayson',
    'Drew',
    'Callen',
    'Jasiah',
    'Drake',
    'Kannon',
    'Braylon',
    'Sonny',
    'Bo',
    'Moshe',
    'Huxley',
    'Quentin',
    'Rowen',
    'Santana',
    'Cannon',
    'Kenzo',
    'Wells',
    'Julio',
    'Nikolai',
    'Conrad',
    'Jalen',
    'Makai',
    'Benson',
    'Derrick',
    'Gerardo',
    'Davis',
    'Abram',
    'Mohamed',
    'Ronald',
    'Raul',
    'Arjun',
    'Dexter',
    'Kaysen',
    'Jaime',
    'Scott',
    'Lawrence',
    'Ariel',
    'Skyler',
    'Danny',
    'Roland',
    'Chandler',
    'Yusuf',
    'Samson',
    'Case',
    'Zain',
    'Roy',
    'Rodrigo',
    'Sutton',
    'Boone',
    'Saint',
    'Saul',
    'Jaziel',
    'Hezekiah',
    'Alec',
    'Arturo',
    'Jamari',
    'Jaxtyn',
    'Julien',
    'Koa',
    'Reece',
    'Landen',
    'Koda',
    'Darius',
    'Sylas',
    'Ares',
    'Kyree',
    'Boston',
    'Keith',
    'Taylor',
    'Johan',
    'Edison',
    'Sincere',
    'Watson',
    'Jerry',
    'Nikolas',
    'Quincy',
    'Shepherd',
    'Brycen',
    'Marvin',
    'Dariel',
    'Axton',
    'Donald',
    'Bodie',
    'Finnley',
    'Onyx',
    'Rayan',
    'Raylan',
    'Brixton',
    'Colby',
    'Shiloh',
    'Valentino',
    'Layton',
    'Trenton',
    'Landyn',
    'Alessandro',
    'Ahmad',
    'Gustavo',
    'Ledger',
    'Ridge',
    'Ander',
    'Ahmed',
    'Kingsley',
    'Issac',
    'Mauricio',
    'Tony',
    'Leonard',
    'Mohammed',
    'Uriah',
    'Duke',
    'Kareem',
    'Lucian',
    'Marcelo',
    'Aarav',
    'Leandro',
    'Reign',
    'Clay',
    'Kohen',
    'Dennis',
    'Samir',
    'Ermias',
    'Otis',
    'Emir',
    'Nixon',
    'Ty',
    'Sam',
    'Fletcher',
    'Wilson',
    'Dustin',
    'Hamza',
    'Bryant',
    'Flynn',
    'Lionel',
    'Mohammad',
    'Cason',
    'Jamir',
    'Aden',
    'Dakari',
    'Justice',
    'Dillon',
    'Layne',
    'Zaid',
    'Alden',
    'Nelson',
    'Devon',
    'Titan',
    'Chris',
    'Khari',
    'Zeke',
    'Noe',
    'Alberto',
    'Roger',
    'Brock',
    'Rex',
    'Quinton',
    'Alvin',
    'Cullen',
    'Azariah',
    'Harlan',
    'Kellan',
    'Lennon',
    'Marcel',
    'Keaton',
    'Morgan',
    'Ricky',
    'Trey',
    'Karsyn',
    'Langston',
    'Miller',
    'Chaim',
    'Salvador',
    'Amias',
    'Tadeo',
    'Curtis',
    'Lachlan',
    'Amos',
    'Anakin',
    'Krew',
    'Tomas',
    'Jefferson',
    'Yosef',
    'Bruno',
    'Korbin',
    'Augustine',
    'Cayson',
    'Mathew',
    'Vihaan',
    'Jamie',
    'Clyde',
    'Brendan',
    'Jagger',
    'Carmelo',
    'Harry',
    'Nathanael',
    'Mitchell',
    'Darren',
    'Ray',
    'Jedidiah',
    'Jimmy',
    'Lochlan',
    'Bellamy',
    'Eddie',
    'Rayden',
    'Reese',
    'Stanley',
    'Joe',
    'Houston',
    'Douglas',
    'Vincenzo',
    'Casen',
    'Emery',
    'Joziah',
    'Leighton',
    'Marcellus',
    'Atreus',
    'Aron',
    'Hugh',
    'Musa',
    'Tommy',
    'Alfredo',
    'Junior',
    'Neil',
    'Westley',
    'Banks',
    'Eliel',
    'Melvin',
    'Maximo',
    'Briar',
    'Colten',
    'Lance',
    'Nova',
    'Trace',
    'Axl',
    'Ramon',
    'Vicente',
    'Brennan',
    'Caspian',
    'Remi',
    'Deandre',
    'Legacy',
    'Lee',
    'Valentin',
    'Ben',
    'Louie',
    'Westin',
    'Wayne',
    'Benicio',
    'Grey',
    'Zayd',
    'Gatlin',
    'Mekhi',
    'Orlando',
    'Bjorn',
    'Harley',
    'Alonso',
    'Rio',
    'Aldo',
    'Byron',
    'Eliseo',
    'Ernesto',
    'Talon',
    'Thaddeus',
    'Brecken',
    'Kace',
    'Kellen',
    'Enoch',
    'Kiaan',
    'Lian',
    'Creed',
    'Rohan',
    'Callahan',
    'Jaxxon',
    'Ocean',
    'Crosby',
    'Dash',
    'Gary',
    'Mylo',
    'Ira',
    'Magnus',
    'Salem',
    'Abdullah',
    'Kye',
    'Tru',
    'Forest',
    'Jon',
    'Misael',
    'Madden',
    'Braden',
    'Carl',
    'Hassan',
    'Emory',
    'Kristian',
    'Alaric',
    'Ambrose',
    'Dario',
    'Allan',
    'Bode',
    'Boden',
    'Juelz',
    'Kristopher',
    'Genesis',
    'Idris',
    'Ameer',
    'Anders',
    'Darian',
    'Kase',
    'Aryan',
    'Dane',
    'Guillermo',
    'Elisha',
    'Jakobe',
    'Thatcher',
    'Eugene',
    'Ishaan',
    'Larry',
    'Wesson',
    'Yehuda',
    'Alvaro',
    'Bobby',
    'Bronson',
    'Dilan',
    'Kole',
    'Kyro',
    'Tristen',
    'Blaze',
    'Brayan',
    'Jadiel',
    'Kamryn',
    'Demetrius',
    'Maurice',
    'Arian',
    'Kabir',
    'Rocky',
    'Rudy',
    'Randy',
    'Rodney',
    'Yousef',
    'Felipe',
    'Robin',
    'Aydin',
    'Dior',
    'Kaiser',
    'Van',
    'Brodie',
    'London',
    'Eithan',
    'Stefan',
    'Ulises',
    'Camilo',
    'Branson',
    'Jakari',
    'Judson',
    'Yahir',
    'Zavier',
    'Damari',
    'Jakob',
    'Jaxx',
    'Bentlee',
    'Cain',
    'Niklaus',
    'Rey',
    'Zahir',
    'Aries',
    'Blaine',
    'Kyng',
    'Castiel',
    'Henrik',
    'Joey',
    'Khalid',
    'Bear',
    'Graysen',
    'Jair',
    'Kylen',
    'Darwin',
    'Alfred',
    'Ayan',
    'Kenji',
    'Zakai',
    'Avi',
    'Cory',
    'Fisher',
    'Jacoby',
    'Osiris',
    'Harlem',
    'Jamal',
    'Santos',
    'Wallace',
    'Brett',
    'Fox',
    'Leif',
    'Maison',
    'Reuben',
    'Adler',
    'Zev',
    'Calum',
    'Kelvin',
    'Zechariah',
    'Bridger',
    'Mccoy',
    'Seven',
    'Shepard',
    'Azrael',
    'Leroy',
    'Terry',
    'Harold',
    'Mac',
    'Mordechai',
    'Ahmir',
    'Cal',
    'Franco',
    'Trent',
    'Blaise',
    'Coen',
    'Dominik',
    'Marley',
    'Davion',
    'Jeremias',
    'Riggs',
    'Jones',
    'Will',
    'Damir',
    'Dangelo',
    'Canaan',
    'Dion',
    'Jabari',
    'Landry',
    'Salvatore',
    'Kody',
    'Hakeem',
    'Truett',
    'Gerald',
    'Lyric',
    'Gordon',
    'Jovanni',
    'Kamdyn',
    'Alistair',
    'Cillian',
    'Foster',
    'Terrance',
    'Murphy',
    'Zyair',
    'Cedric',
    'Rome',
    'Abner',
    'Colter',
    'Dayton',
    'Jad',
    'Xzavier',
    'Rene',
    'Vance',
    'Duncan',
    'Frankie',
    'Bishop',
    'Davian',
    'Everest',
    'Heath',
    'Jaxen',
    'Marlon',
    'Maxton',
    'Reginald',
    'Harris',
    'Jericho',
    'Keenan',
    'Korbyn',
    'Wes',
    'Eliezer',
    'Jeffery',
    'Kalel',
    'Kylian',
    'Turner',
    'Willie',
    'Rogelio',
    'Ephraim',
    )

female_first_name = (
    'Olivia',
    'Emma',
    'Ava',
    'Charlotte',
    'Sophia',
    'Amelia',
    'Isabella',
    'Mia',
    'Evelyn',
    'Harper',
    'Camila',
    'Gianna',
    'Abigail',
    'Luna',
    'Ella',
    'Elizabeth',
    'Sofia',
    'Emily',
    'Avery',
    'Mila',
    'Scarlett',
    'Eleanor',
    'Madison',
    'Layla',
    'Penelope',
    'Aria',
    'Chloe',
    'Grace',
    'Ellie',
    'Nora',
    'Hazel',
    'Zoey',
    'Riley',
    'Victoria',
    'Lily',
    'Aurora',
    'Violet',
    'Nova',
    'Hannah',
    'Emilia',
    'Zoe',
    'Stella',
    'Everly',
    'Isla',
    'Leah',
    'Lillian',
    'Addison',
    'Willow',
    'Lucy',
    'Paisley',
    'Natalie',
    'Naomi',
    'Eliana',
    'Brooklyn',
    'Elena',
    'Aubrey',
    'Claire',
    'Ivy',
    'Kinsley',
    'Audrey',
    'Maya',
    'Genesis',
    'Skylar',
    'Bella',
    'Aaliyah',
    'Madelyn',
    'Savannah',
    'Anna',
    'Delilah',
    'Serenity',
    'Caroline',
    'Kennedy',
    'Valentina',
    'Ruby',
    'Sophie',
    'Alice',
    'Gabriella',
    'Sadie',
    'Ariana',
    'Allison',
    'Hailey',
    'Autumn',
    'Nevaeh',
    'Natalia',
    'Quinn',
    'Josephine',
    'Sarah',
    'Cora',
    'Emery',
    'Samantha',
    'Piper',
    'Leilani',
    'Eva',
    'Everleigh',
    'Madeline',
    'Lydia',
    'Jade',
    'Peyton',
    'Brielle',
    'Adeline',
    'Vivian',
    'Rylee',
    'Clara',
    'Raelynn',
    'Melanie',
    'Melody',
    'Julia',
    'Athena',
    'Maria',
    'Liliana',
    'Hadley',
    'Arya',
    'Rose',
    'Reagan',
    'Eliza',
    'Adalynn',
    'Kaylee',
    'Lyla',
    'Mackenzie',
    'Alaia',
    'Isabelle',
    'Charlie',
    'Arianna',
    'Mary',
    'Remi',
    'Margaret',
    'Iris',
    'Parker',
    'Ximena',
    'Eden',
    'Ayla',
    'Kylie',
    'Elliana',
    'Josie',
    'Katherine',
    'Faith',
    'Alexandra',
    'Eloise',
    'Adalyn',
    'Amaya',
    'Jasmine',
    'Amara',
    'Daisy',
    'Reese',
    'Valerie',
    'Brianna',
    'Cecilia',
    'Andrea',
    'Summer',
    'Valeria',
    'Norah',
    'Ariella',
    'Esther',
    'Ashley',
    'Emerson',
    'Aubree',
    'Isabel',
    'Anastasia',
    'Ryleigh',
    'Khloe',
    'Taylor',
    'Londyn',
    'Lucia',
    'Emersyn',
    'Callie',
    'Sienna',
    'Blakely',
    'Kehlani',
    'Genevieve',
    'Alina',
    'Bailey',
    'Juniper',
    'Maeve',
    'Molly',
    'Harmony',
    'Georgia',
    'Magnolia',
    'Catalina',
    'Freya',
    'Juliette',
    'Sloane',
    'June',
    'Sara',
    'Ada',
    'Kimberly',
    'River',
    'Ember',
    'Juliana',
    'Aliyah',
    'Millie',
    'Brynlee',
    'Teagan',
    'Morgan',
    'Jordyn',
    'London',
    'Alaina',
    'Olive',
    'Rosalie',
    'Alyssa',
    'Ariel',
    'Finley',
    'Arabella',
    'Journee',
    'Hope',
    'Leila',
    'Alana',
    'Gemma',
    'Vanessa',
    'Gracie',
    'Noelle',
    'Marley',
    'Elise',
    'Presley',
    'Kamila',
    'Zara',
    'Amy',
    'Kayla',
    'Payton',
    'Blake',
    'Ruth',
    'Alani',
    'Annabelle',
    'Sage',
    'Aspen',
    'Laila',
    'Lila',
    'Rachel',
    'Trinity',
    'Daniela',
    'Alexa',
    'Lilly',
    'Lauren',
    'Elsie',
    'Margot',
    'Adelyn',
    'Zuri',
    'Brooke',
    'Sawyer',
    'Lilah',
    'Lola',
    'Selena',
    'Mya',
    'Sydney',
    'Diana',
    'Ana',
    'Vera',
    'Alayna',
    'Nyla',
    'Elaina',
    'Rebecca',
    'Angela',
    'Kali',
    'Alivia',
    'Raegan',
    'Rowan',
    'Phoebe',
    'Camilla',
    'Joanna',
    'Malia',
    'Vivienne',
    'Dakota',
    'Brooklynn',
    'Evangeline',
    'Camille',
    'Jane',
    'Nicole',
    'Catherine',
    'Jocelyn',
    'Julianna',
    'Lena',
    'Lucille',
    'Mckenna',
    'Paige',
    'Adelaide',
    'Charlee',
    'Mariana',
    'Myla',
    'Mckenzie',
    'Tessa',
    'Miriam',
    'Oakley',
    'Kailani',
    'Alayah',
    'Amira',
    'Adaline',
    'Phoenix',
    'Milani',
    'Annie',
    'Lia',
    'Angelina',
    'Harley',
    'Cali',
    'Maggie',
    'Hayden',
    'Leia',
    'Fiona',
    'Briella',
    'Journey',
    'Lennon',
    'Saylor',
    'Jayla',
    'Kaia',
    'Thea',
    'Adriana',
    'Mariah',
    'Juliet',
    'Oaklynn',
    'Kiara',
    'Alexis',
    'Haven',
    'Aniyah',
    'Delaney',
    'Gracelynn',
    'Kendall',
    'Winter',
    'Lilith',
    'Logan',
    'Amiyah',
    'Evie',
    'Alexandria',
    'Gracelyn',
    'Gabriela',
    'Sutton',
    'Harlow',
    'Madilyn',
    'Makayla',
    'Evelynn',
    'Gia',
    'Nina',
    'Amina',
    'Giselle',
    'Brynn',
    'Blair',
    'Amari',
    'Octavia',
    'Michelle',
    'Talia',
    'Demi',
    'Alaya',
    'Kaylani',
    'Izabella',
    'Fatima',
    'Tatum',
    'Makenzie',
    'Lilliana',
    'Arielle',
    'Palmer',
    'Melissa',
    'Willa',
    'Samara',
    'Destiny',
    'Dahlia',
    'Celeste',
    'Ainsley',
    'Rylie',
    'Reign',
    'Laura',
    'Adelynn',
    'Gabrielle',
    'Remington',
    'Wren',
    'Brinley',
    'Amora',
    'Lainey',
    'Collins',
    'Lexi',
    'Aitana',
    'Alessandra',
    'Kenzie',
    'Raelyn',
    'Elle',
    'Everlee',
    'Haisley',
    'Hallie',
    'Wynter',
    'Daleyza',
    'Gwendolyn',
    'Paislee',
    'Ariyah',
    'Veronica',
    'Heidi',
    'Anaya',
    'Cataleya',
    'Kira',
    'Avianna',
    'Felicity',
    'Aylin',
    'Miracle',
    'Sabrina',
    'Lana',
    'Ophelia',
    'Elianna',
    'Royalty',
    'Madeleine',
    'Esmeralda',
    'Joy',
    'Kalani',
    'Esme',
    'Jessica',
    'Leighton',
    'Ariah',
    'Makenna',
    'Nylah',
    'Viviana',
    'Camryn',
    'Cassidy',
    'Dream',
    'Luciana',
    'Maisie',
    'Stevie',
    'Kate',
    'Lyric',
    'Daniella',
    'Alicia',
    'Daphne',
    'Frances',
    'Charli',
    'Raven',
    'Paris',
    'Nayeli',
    'Serena',
    'Heaven',
    'Bianca',
    'Helen',
    'Hattie',
    'Averie',
    'Mabel',
    'Selah',
    'Allie',
    'Marlee',
    'Kinley',
    'Regina',
    'Carmen',
    'Jennifer',
    'Jordan',
    'Alison',
    'Stephanie',
    'Maren',
    'Kayleigh',
    'Angel',
    'Annalise',
    'Jacqueline',
    'Braelynn',
    'Emory',
    'Rosemary',
    'Scarlet',
    'Amanda',
    'Danielle',
    'Emelia',
    'Ryan',
    'Carolina',
    'Astrid',
    'Kensley',
    'Shiloh',
    'Maci',
    'Francesca',
    'Rory',
    'Celine',
    'Kamryn',
    'Zariah',
    'Liana',
    'Poppy',
    'Maliyah',
    'Keira',
    'Skyler',
    'Noa',
    'Skye',
    'Nadia',
    'Addilyn',
    'Rosie',
    'Eve',
    'Sarai',
    'Edith',
    'Jolene',
    'Maddison',
    'Meadow',
    'Charleigh',
    'Matilda',
    'Elliott',
    'Madelynn',
    'Holly',
    'Leona',
    'Azalea',
    'Katie',
    'Mira',
    'Ari',
    'Kaitlyn',
    'Danna',
    'Cameron',
    'Kyla',
    'Bristol',
    'Kora',
    'Armani',
    'Nia',
    'Malani',
    'Dylan',
    'Remy',
    'Maia',
    'Dior',
    'Legacy',
    'Alessia',
    'Shelby',
    'Maryam',
    'Sylvia',
    'Yaretzi',
    'Lorelei',
    'Madilynn',
    'Abby',
    'Helena',
    'Jimena',
    'Elisa',
    'Renata',
    'Amber',
    'Aviana',
    'Carter',
    'Emmy',
    'Haley',
    'Alondra',
    'Elaine',
    'Erin',
    'April',
    'Emely',
    'Imani',
    'Kennedi',
    'Lorelai',
    'Hanna',
    'Kelsey',
    'Aurelia',
    'Colette',
    'Jaliyah',
    'Kylee',
    'Macie',
    'Aisha',
    'Dorothy',
    'Charley',
    'Kathryn',
    'Adelina',
    'Adley',
    'Monroe',
    'Sierra',
    'Ailani',
    'Miranda',
    'Mikayla',
    'Alejandra',
    'Amirah',
    'Jada',
    'Jazlyn',
    'Jenna',
    'Jayleen',
    'Beatrice',
    'Kendra',
    'Lyra',
    'Nola',
    'Emberly',
    'Mckinley',
    'Myra',
    'Katalina',
    'Antonella',
    'Zelda',
    'Alanna',
    'Amaia',
    'Priscilla',
    'Briar',
    'Kaliyah',
    'Itzel',
    'Oaklyn',
    'Alma',
    'Mallory',
    'Novah',
    'Amalia',
    'Fernanda',
    'Alia',
    'Angelica',
    'Elliot',
    'Justice',
    'Mae',
    'Cecelia',
    'Gloria',
    'Ariya',
    'Virginia',
    'Cheyenne',
    'Aleah',
    'Jemma',
    'Henley',
    'Meredith',
    'Leyla',
    'Lennox',
    'Ensley',
    'Zahra',
    'Reina',
    'Frankie',
    'Lylah',
    'Nalani',
    'Reyna',
    'Saige',
    'Ivanna',
    'Aleena',
    'Emerie',
    'Ivory',
    'Leslie',
    'Alora',
    'Ashlyn',
    'Bethany',
    'Bonnie',
    'Sasha',
    'Xiomara',
    'Salem',
    'Adrianna',
    'Dayana',
    'Clementine',
    'Karina',
    'Karsyn',
    'Emmie',
    'Julie',
    'Julieta',
    'Briana',
    'Carly',
    'Macy',
    'Marie',
    'Oaklee',
    'Christina',
    'Malaysia',
    'Ellis',
    'Irene',
    'Anne',
    'Anahi',
    'Mara',
    'Rhea',
    'Davina',
    'Dallas',
    'Jayda',
    'Mariam',
    'Skyla',
    'Siena',
    'Elora',
    'Marilyn',
    'Jazmin',
    'Megan',
    'Rosa',
    'Savanna',
    'Allyson',
    'Milan',
    'Coraline',
    'Johanna',
    'Melany',
    'Chelsea',
    'Michaela',
    'Melina',
    'Angie',
    'Cassandra',
    'Yara',
    'Kassidy',
    'Liberty',
    'Lilian',
    'Avah',
    'Anya',
    'Laney',
    'Navy',
    'Opal',
    'Amani',
    'Zaylee',
    'Mina',
    'Sloan',
    'Romina',
    'Ashlynn',
    'Aliza',
    'Liv',
    'Malaya',
    'Blaire',
    'Janelle',
    'Kara',
    'Analia',
    'Hadassah',
    'Hayley',
    'Karla',
    'Chaya',
    'Cadence',
    'Kyra',
    'Alena',
    'Ellianna',
    'Katelyn',
    'Kimber',
    'Laurel',
    'Lina',
    'Capri',
    'Braelyn',
    'Faye',
    'Kamiyah',
    'Kenna',
    'Louise',
    'Calliope',
    'Kaydence',
    'Nala',
    'Tiana',
    'Aileen',
    'Sunny',
    'Zariyah',
    'Milana',
    'Giuliana',
    'Eileen',
    'Elodie',
    'Rayna',
    'Monica',
    'Galilea',
    'Journi',
    'Lara',
    'Marina',
    'Aliana',
    'Harmoni',
    'Jamie',
    'Holland',
    'Emmalyn',
    'Lauryn',
    'Chanel',
    'Tinsley',
    'Jessie',
    'Lacey',
    'Elyse',
    'Janiyah',
    'Jolie',
    'Ezra',
    'Marleigh',
    'Roselyn',
    'Lillie',
    'Louisa',
    'Madisyn',
    'Penny',
    'Kinslee',
    'Treasure',
    'Zaniyah',
    'Estella',
    'Jaylah',
    'Khaleesi',
    'Alexia',
    'Dulce',
    'Indie',
    'Maxine',
    'Waverly',
    'Giovanna',
    'Miley',
    'Saoirse',
    'Estrella',
    'Greta',
    'Rosalia',
    'Mylah',
    'Teresa',
    'Bridget',
    'Kelly',
    'Adalee',
    'Aubrie',
    'Lea',
    'Harlee',
    'Anika',
    'Itzayana',
    'Hana',
    'Kaisley',
    'Mikaela',
    'Naya',
    'Avalynn',
    'Margo',
    'Sevyn',
    'Florence',
    'Keilani',
    'Lyanna',
    'Joelle',
    'Kataleya',
    'Royal',
    'Averi',
    'Kallie',
    'Winnie',
    'Baylee',
    'Martha',
    'Pearl',
    'Alaiya',
    'Rayne',
    'Sylvie',
    'Brylee',
    'Jazmine',
    'Ryann',
    'Kori',
    'Noemi',
    'Haylee',
    'Julissa',
    'Celia',
    'Laylah',
    'Rebekah',
    'Rosalee',
    'Aya',
    'Bria',
    'Adele',
    'Aubrielle',
    'Tiffany',
    'Addyson',
    'Kai',
    'Bellamy',
    'Leilany',
    'Princess',
    'Chana',
    'Estelle',
    'Selene',
    'Sky',
    'Dani',
    'Thalia',
    'Ellen',
    'Rivka',
    'Amelie',
    'Andi',
    'Kynlee',
    'Raina',
    'Vienna',
    'Alianna',
    'Livia',
    'Madalyn',
    'Mercy',
    'Novalee',
    'Ramona',
    'Vada',
    'Berkley',
    'Gwen',
    'Persephone',
    'Milena',
    'Paula',
    'Clare',
    'Kairi',
    'Linda',
    'Paulina',
    'Kamilah',
    'Amoura',
    'Hunter',
    'Isabela',
    'Karen',
    'Marianna',
    'Sariyah',
    'Theodora',
    'Annika',
    'Kyleigh',
    'Nellie',
    'Scarlette',
    'Keyla',
    'Kailey',
    'Mavis',
    'Lilianna',
    'Rosalyn',
    'Sariah',
    'Tori',
    'Yareli',
    'Aubriella',
    'Bexley',
    'Bailee',
    'Jianna',
    'Keily',
    'Annabella',
    'Azariah',
    'Denisse',
    'Promise',
    'August',
    'Hadlee',
    'Halle',
    'Fallon',
    'Oakleigh',
    'Zaria',
    'Jaylin',
    'Paisleigh',
    'Crystal',
    'Ila',
    'Aliya',
    'Cynthia',
    'Giana',
    'Maleah',
    'Rylan',
    'Aniya',
    'Denise',
    'Emmeline',
    'Scout',
    'Simone',
    'Noah',
    'Zora',
    'Meghan',
    'Landry',
    'Ainhoa',
    'Lilyana',
    'Noor',
    'Belen',
    'Brynleigh',
    'Cleo',
    'Meilani',
    'Karter',
    'Amaris',
    'Frida',
    'Iliana',
    'Violeta',
    'Addisyn',
    'Nancy',
    'Denver',
    'Leanna',
    'Braylee',
    'Kiana',
    'Wrenley',
    'Barbara',
    'Khalani',
    'Aspyn',
    'Ellison',
    'Judith',
    'Robin',
    'Valery',
    'Aila',
    'Deborah',
    'Cara',
    'Clarissa',
    'Iyla',
    'Lexie',
    'Anais',
    'Kaylie',
    'Nathalie',
    'Alisson',
    'Della',
    'Addilynn',
    'Elsa',
    'Zoya',
    'Layne',
    'Marlowe',
    'Jovie',
    'Kenia',
    'Samira',
    'Jaylee',
    'Jenesis',
    'Etta',
    'Shay',
    'Amayah',
    'Avayah',
    'Egypt',
    'Flora',
    'Raquel',
    'Whitney',
    'Zola',
    'Giavanna',
    'Raya',
    'Veda',
    'Halo',
    'Paloma',
    'Nataly',
    'Whitley',
    'Dalary',
    'Drew',
    'Guadalupe',
    'Kamari',
    'Esperanza',
    'Loretta',
    'Malayah',
    'Natasha',
    'Stormi',
    'Ansley',
    'Carolyn',
    'Corinne',
    'Paola',
    'Brittany',
    'Emerald',
    'Freyja',
    'Zainab',
    'Artemis',
    'Jillian',
    'Kimora',
    'Zoie',
    'Aislinn',
    'Emmaline',
    'Ayleen',
    'Queen',
    'Jaycee',
    'Murphy',
    'Nyomi',
    'Elina',
    'Hadleigh',
    'Marceline',
    'Marisol',
    'Yasmin',
    'Zendaya',
    'Chandler',
    'Emani',
    'Jaelynn',
    'Kaiya',
    'Nathalia',
    'Violette',
    'Joyce',
    'Paityn',
    'Elisabeth',
    'Emmalynn',
    'Luella',
    'Yamileth',
    'Aarya',
    'Luisa',
    'Zhuri',
    'Araceli',
    'Harleigh',
    'Madalynn',
    'Melani',
    'Laylani',
    'Magdalena',
    'Mazikeen',
    'Belle',
    'Kadence',
    )

last_name = (
    'Smith',
    'Johnson',
    'Williams',
    'Brown',
    'Jones',
    'Garcia',
    'Miller',
    'Davis',
    'Rodriguez',
    'Martinez',
    'Hernandez',
    'Lopez',
    'Gonzales',
    'Wilson',
    'Anderson',
    'Thomas',
    'Taylor',
    'Moore',
    'Jackson',
    'Martin',
    'Lee',
    'Perez',
    'Thompson',
    'White',
    'Harris',
    'Sanchez',
    'Clark',
    'Ramirez',
    'Lewis',
    'Robinson',
    'Walker',
    'Young',
    'Allen',
    'King',
    'Wright',
    'Scott',
    'Torres',
    'Nguyen',
    'Hill',
    'Flores',
    'Green',
    'Adams',
    'Nelson',
    'Baker',
    'Hall',
    'Rivera',
    'Campbell',
    'Mitchell',
    'Carter',
    'Roberts',
    'Gomez',
    'Phillips',
    'Evans',
    'Turner',
    'Diaz',
    'Parker',
    'Cruz',
    'Edwards',
    'Collins',
    'Reyes',
    'Stewart',
    'Morris',
    'Morales',
    'Murphy',
    'Cook',
    'Rogers',
    'Gutierrez',
    'Ortiz',
    'Morgan',
    'Cooper',
    'Peterson',
    'Bailey',
    'Reed',
    'Kelly',
    'Howard',
    'Ramos',
    'Kim',
    'Cox',
    'Ward',
    'Richardson',
    'Watson',
    'Brooks',
    'Chavez',
    'Wood',
    'James',
    'Bennet',
    'Gray',
    'Mendoza',
    'Ruiz',
    'Hughes',
    'Price',
    'Alvarez',
    'Castillo',
    'Sanders',
    'Patel',
    'Myers',
    'Long',
    'Ross',
    'Foster',
    'Jimenez',
    )

state_names = (
    'Alaska',
    'Alabama',
    'Arkansas',
    'American Samoa',
    'Arizona',
    'California',
    'Colorado',
    'Connecticut',
    'District of Columbia',
    'Delaware',
    'Florida',
    'Georgia',
    'Guam',
    'Hawaii',
    'Iowa',
    'Idaho',
    'Illinois',
    'Indiana',
    'Kansas',
    'Kentucky',
    'Louisiana',
    'Massachusetts',
    'Maryland',
    'Maine',
    'Minnesota',
    'Missouri',
    'Mississippi',
    'Montana',
    'North Carolina',
    'North Dakota',
    'Nebraska',
    'New Hampshire',
    'New Jersey',
    'New Mexico',
    'Nevada',
    'New York',
    'Ohio',
    'Oklahoma',
    'Oregon',
    'Pennsylvania',
    'Puerto Rico',
    'Rhode Island',
    'South Carolina',
    'South Dakota',
    'Tennessee',
    'Texas',
    'Utah',
    'Virginia',
    'Virgin Islands',
    'Vermont',
    'Washington',
    'Wisconsin',
    'West Virginia',
    'Wyoming',
    'Michigan',
    )

convictions = ('Misdemeanors', 'Felony', 'Wobbler')

skills = (
    'HTML',
    'CSS',
    'JavaScript',
    'Python',
    'Ruby',
    'C++',
    'Axios',
    'React',
    'Node.JS',
    'C#',
    'Django',
    'MongoDB',
    'SQL',
    'PostgreSQL',
    'NoSQL',
    'PHP',
    'Angular',
    'Microsoft Azure',
    'IOS',
    'Android',
    )

time_zones = ('Pacific', 'Mountain', 'Central', 'Eastern')

purpose = ('Technical', 'Career Preparation')

exp_level = ('Beginner', 'Intermediate', 'Advanced', 'Unsure')

# + [markdown] id="We530RIhtbou"
# Now that we have some source data out of the way, we can get to the fun part, creating the Mentor and Mentee classes that we will use to populate our DataFrame

# + id="MIVpP2cdF3TJ"
import random as r
import pandas as pd


class Mentee:

    email_end = '@fake.com'

    def __init__(self):
        self.profile_id = 'E' + str(r.randint(1000000, 70000000000000))
        self.tech_or_career = r.sample(purpose, k=r.randint(1, 2))
        self.experience = r.sample(exp_level, k=1)

        self.first_name = r.choice(male_first_name)
        self.last_name = r.choice(last_name)
        self.full_name = self.first_name + ' ' + self.last_name
        self.time_zone = r.sample(time_zones, k=1)

        self.email = self.profile_id + self.last_name.lower() \
            + self.email_end

        self.incarcerated = bool(r.randint(0, 1))
        if self.incarcerated:
            self.list_convictions = r.choice(convictions)
        else:
            self.list_convictions = 'None'

        self.desired_skills = r.sample(skills, k=3)

    @classmethod
    def to_df(cls, num_rows):
        return pd.DataFrame(vars(cls()) for _ in range(num_rows))


# + id="uq1FwVSsFIZ3"
class Mentor:

    def __init__(self):
        self.profile_id = 'O' + str(hash(r.randint(2000000,
                                    70000000000000000)))
        self.skills = sorted(r.sample(skills, k=r.randint(1, 4)))
        self.career_capable = bool(r.randint(0, 1))
        self.skill_rank = sorted(r.sample(exp_level, k=r.randint(1, 4)))
        self.time_zone = r.sample(time_zones, k=1)

    @classmethod
    def to_df(cls, num_rows):
        return pd.DataFrame(vars(cls()) for _ in range(num_rows))


# + colab={"base_uri": "https://localhost:8080/", "height": 423} id="AOPgAyEkaJQo" outputId="5a25dca2-105c-4d5d-a218-35ee81ccbf10"
mentor = Mentor()

mentor_df = mentor.to_df(500)
mentor_df

# + colab={"base_uri": "https://localhost:8080/", "height": 658} id="sYVwE1KHXHv7" outputId="7f659a55-af3a-4c2f-e344-fabe719b7ae3"
mentee = Mentee()
mentee_df = mentee.to_df(1500)
mentee_df

# + [markdown] id="1Lou24FEuy3P"
# # Dan Kositzke Notebook Add-On's

# + [markdown] id="Ri9FRXjbu5Vm"
# ## Using Euclidean Distance to suggest top 5 mentees for each mentor

# + [markdown] id="H8RaG3R6vBp8"
# In a multi-dimensional space, we can plot the data points of 1 mentor along with all of the mentees. We can then compute the euclidean distance between each point. The 5 mentee data points that are spatially closest to the mentor data point will be the recommendations. Admin can then view the recommendations and make the final pairing decision.

# + [markdown] id="xJUmieNBwUCf"
# ![6198d9c0c8439c795c6c051ec32d272a9e1fe9ce.jpeg](data:image/jpeg;base64,/9j/4AAQSkZJRgABAQEAYABgAAD/2wBDAAYEBQYFBAYGBQYHBwYIChAKCgkJChQODwwQFxQYGBcUFhYaHSUfGhsjHBYWICwgIyYnKSopGR8tMC0oMCUoKSj/2wBDAQcHBwoIChMKChMoGhYaKCgoKCgoKCgoKCgoKCgoKCgoKCgoKCgoKCgoKCgoKCgoKCgoKCgoKCgoKCgoKCgoKCj/wAARCAHgAlgDASIAAhEBAxEB/8QAHAAAAQQDAQAAAAAAAAAAAAAAAAIDBgcBBAUI/8QAVxAAAgEDAgMEBwUEBgYHBwALAQIDAAQRBRIGITEHE0FRIjIzYXFysRRSgZHBI0Kh0QgVNGKCoiRDc5Ky4RY2U2N0wvEXJSY1RGSzg6M3RlR1k9Kk0+L/xAAaAQEAAgMBAAAAAAAAAAAAAAAAAQUCAwQG/8QANhEAAgEDAgQDBwQCAgIDAAAAAAECAwQRITEFEkFRYXHwEyKBkaHB0RRCsfEy4QYjFVIWM2L/2gAMAwEAAhEDEQA/APVNFFFAFFFFAFFFFAFFFFAFFFFAFFFFAFFFFAFFFFAFFFFAFFFFAFFFFAFFFFAFFFUH248KaZqF7HcaPfXV12om4hfThbXT95bxd5yzEGKxQqpYlyBluZJLYJbpdx0bL8oqMdoc2n2fZ7rNzxHbW17Z21k800U8SyJIyrkeiwwTuAx78VAOxnsr4YHZNoSa/wAN6VeX95a9/PPc2aGb9rlgN5G4EKwAwQRjwotc+GPrn8DovH7Y/Jc1FVF2a61faP2q8T9n97f3Wo2NrAmo6bNdSGWaKJtu6JpG5sAXG3JJAGMnwt2nRNbMdWn0CiqH7M/6g4r4v4u0ztC06zvuMrfUJQlvqkImKWYOYhbhwQEAJPoYzkMc5BqzeCOHG4XTXGur+8uo7i9eeKW+umneKAKu2Pe5J2qd+Mnx+NFhpPus/wAevgw9G1449euqJXRUasuONAvtRtbO1u5na7YpbXH2SYW1wwUtiK4Kd0/IEjaxzg46V0Nc4g03Q+5XUJ37+bPc20EL3E8oGNxSKNWdgMjJAIHjigOrRXDsOK9G1G2u5tPu2uxaRLNcRQQSSSxBgSFaMKXEnon9njePEVF+B+0i34pvuIbmGz1eLSrBjFb7tLuCZe65SuCEOWLMFEWd+EztBJAdcDpksSioF2dcfRca6zrf2S11KDT7aX7Pam4sJY1l7s4kcyFdoJZgojJ3AJkgZIHW13jzh3Q3uVv72Ui0/tT2tpNcpa+OJniRliOCDhyOXPpTt4gk9FR66414cttd0/RX1i1fVr8gW9pC3eyMCu8MQudqleYZsA+dbHD3FGi8Rz6jFoeoRXrafN9nuTECVSTGdobGG/Any60B2aKj3aBxXZcE8I6jr+pAtDaJlY1ODK5OFQe8kge7r4VFODOEbnifSbfXO0wJq1/eos6aVMM2NipBKqsByrSAMcu4ZvAHlzLXOOnr1/QemM9SzKKg44A03TuK9F1Hh6A6VZW7SvdWNk3c2k7FNqM8CkIXBOQ23PLmeS46Ft2gcJ3U2rR22vWMw0qITXs0b7oYFJIGZR6Gcg+iDn3UbSGpKKK5FhxLo19wzDxDDqECaLLF363k5MKBPvHfjaPjitXSOMtE1bUY7C1nuY7uVDJDHd2U9r36jq0RlRRIACCSmeRB6GnXHUZ0ySGiuDPxhoEHFltw1JqUQ1y4VmjtQrEnau4gsBtDbSG2kg4IOMGnzxJpA1u+0lr1FvrG2W8uVZWCwxMThmcjaOhOM5wM4xTxB16KiNn2kcJ363p03V11D7JKIXFjBLcGRyu7bEI1JlwuSe73YAJOK62i8TaLrXDq67puowS6QUaQ3LHYqKud27dgrjBzuxjHOg3OxRUb0Ljjh/XJLOPT72TvbwF7WO4tpbdrhAu4vGJFUumP31yvMc+YqSUxgBRRRQBRRRQBRRRQBRRRQBRRRQBRRRQBRRRQBRRRQBRRRQBRRRQBRRRQBRRRQBRRRQBRRRQBRRRQBRRRQBRRRQBRRRQBRRRQBRRRQBRRRQBRRRQBRRRQBRRRQGlq2q6do9sLjV7+0sLdnEYlupliQsei5YgZPlVNcecK6bofavwLecCW0Oma/eXpW/gsv2cc1iPSleSNfRxy645kjOSBi1+MOFNE4y0g6XxLp8d9Zb1kCMzIVYdCrKQwPUcj0JHQ1q8F8CcMcEwSxcL6Pb2Hen9pIpZ5H9xkcliPIZwKR0kpPp6/vwEtsLr69eJCv6Rdy97oGh8I2zkXXEuqQ2ZCnmIFYNI3wGFz8as28urDQtIe4vJ4bLTrOLLSSMFSNFGOZqN612a8M61r8et6jb6jJqsRJhuF1a7jaDPUR7ZQIx7lwKdj7POGft8F5eWNxqdxbg9wdWvri/WEkqSyLO7hWyq+kADy61Ec8uOrf2WPXiS90+iXr7fIhXZBpV5rnHfFHaPqFpLZ2+rBLTSYp1KyG0QAd6VPNQ+1SAfeehBNi8Y8Q2/DOkxX928aRPd29sWkOFXvJVQk/AMT+Fdyudrmh6Xr1tHba3p9rqFtHJ3ohuYxJHuwQCVPI8ieo9/UVlthLZY+X+yN8t7v0vkVl/SM4VsrnhOfjC1nbTOJeH4/tNnqEJ2uQp9k33gcnA8CfIkFninXJtabsu0LiXbZ2/ESi51OJ/RWZ44lcWxB/daRgCvjgL41OYuz/hxJoHktLq5it3EkNrd39xcW0TD1SkEkjRrt/dwvo8sYxW7xlwhoPGmlrp3E2nRX9oriRVZmRkYeKspDDy5HmOVQvd+afrz0+XiHrv2a/Hy+4zq9vw7fcQ6eL2NLjVdFR7y3RC5+yhl27mC+iCRnbv67WK+qcRDss1myk4QfjvW7qKTUdflYghgzIgdlhtIvPaAfRHMsWJ55qdcK8L6Jwno66Vw7p0FjYgljHGCS7HqzMcljgAZJJwAPCuLw92X8GcO32oXmjaBa21zfqyTuGdvRbO5U3EiMHJ5JgdPIUemeX1/emvh44G6WfXrt/ZAOzvXU0bsi4w49uERLvVbi71gQllyqklIUyPAlOviSa7nC8idnH9H83EzRve6fpz3dwN+SbmRe82sfMtIo+BFSwdn/AAyODZeFTpzNoUgUPbtczMSFIKjvC+/A2rgbuQAHTlW5qXCGianwtLw5f2jz6RKAJInuJC8hDBstJu3ltwBLFsnxJqJLKlFdUkvJaevImL1Tl3bfx9P5lXTXN32Z/wBGSSXT3X+urazRpnDbjFcXDqWZveO9zz8h4U9DoQuOz3RtI13V9J0jhO67qL7PpUz3dxqzP6WPtBVCTIxyypGzEBjvwTi1o9B0xdDfR3tEn06RDHJDckzd6D13s5JcnxLEk1wODOzHg3gu7e74b0G3tLt+Xfu7zSKMEEK0jMVBB5gEZ8azbTlJvr6x6+WiMVlRS6rP219fMiepWw4k7dLPSLcKmk8NaOTN3bEFJLggCMY6ZjQD5Scc8EWrZafZWBnNjaW9sZ3EkphiVO8bAXc2BzOABk+AFaumaDpumanqmo2Vt3d7qciSXcpdmMrKu1epOABywMCunWKeiXrV5Jxr67YKa/pW6dd3vZlFc20TT22n6hDd3kSjJaFdwY48gWBPu5+FWxZXFprOjQ3FnN3tjeQB45YJCu5GXkVZSCOR6ggitxlDqVYBlIwQRkEVEYeznhy27xdOh1LTYHYubfTdWu7OAE9SsUUqoufcBULZr4/RL7B6tPtp9yBdilhJrfE3FmuPrPEVxo9lqr2Wl2tzq9zJEojA3uQz/tASeQbIHxre7HrYcU6txbxbfJHLZahqskdmnVZYoVEKOR0IwGx8zHyxZmjaFpmi6NHpWkWUVnp6KUWKAbevU5HMsepbOSeZOaVw9oun8O6Na6Vo1sLawtl2RRBmbaMk9WJJOSTknNStPlj+Mv6B658Xn+dPr9CttdsYdX7ZuG+FTFDb8PaJpZ1dLCNAsU0ok7qIbAMbY+oHQHFO8Y3DcQ9s/CGi6Wd50Ey6pqcyHlArRlI4yfBnyfR+7z6VOuIOGNJ1+a0n1GCX7VaFjBc21zLbTxhhhgssTK4UjqucHAyOQrY0HQtM0C0e30izjtkkcySsMs8znq8jnLO58WYknxNF0z0y/N50+WnyxsHrnHVY+mv3+ZWNg1pf9t+uao0SQ6VwpZi0iVIwA95dN3krKB1c5C+ZZvEmnexu6jnfjnjHUpolk1HUJGBDj0bW2Hdr49AVkGfHGfGpxYcE8P2HEF3rVrYFNQu5TPKxnkaMyldveCIsUV9uRuCg4LDPM5rPtdbhfs37Lr/hnQri20u61ki1hgku2d1SV8SSemxZYwDISeSgk9Caxy4xwt8Y+Lef5+hlhSbb2zl+SWPx8Ta7ImsOGezTVePtfCW9xrE1xq9xI55rHI5Mca58wEwPEsPdWz2a8MRxdmU2g8Wk2l9xZLeXUlnuKvGJgWKDyZUwT5HNSThPgLhG103SJ9KR9RsrZElsjLqM15bIR6ssUbyNGp8QygEZOCM1I9b4e0vXHgk1K27ya3DCCZJHjlgLY3NG6EMjYAG5SDjIzgnOc0tUttvh6x8vMwTbxJ75z8fTfpFfdj8t/Ff33CfFMcd1q/CIjitNRTpPayoRGSPB9qYIPkOvMm1q5XD/AA/pugRTppkDo1w/eTzTTPPNM2MAvLIWdyAABknAAA5V1aN51e4SxtsFFFFQSFFFFAFFFFAFFFFAFFFFAFFFFAFFFFAFFFFAFFFFAFFFFAFFFFAFFFFAFFFFAFFFFAFFFFAFFFFAFFFFAFFFFAFFFFAFFFFAFFFFAFFFFAFFFFAFFFFAFFFM3d1b2cRlu54oIx+9I4UfmaAeoqNXvGelwZFv312w/wCyTC/7zYH5ZrgT8Z6pfO0emW0cfge7Vp3H4jAH4g0BYlFVk+k69q/PUZ2EbdRcS5H/APTT0fpSdO4Zk+130MWpSwtbuqgxKVByit0De/zoCz6KgB0XXLcFrfX53wM4dn/VmpQTi+HBTUbeVfI7f/8AWPrQE9oqCf1txdAQGsrWb/Cv6SD6UscV63CP9I0F3I/7PePorUBOKKhK8epH/bNKuYfP0h/5gtbNvx/o8p5rdJ8VVv8AhY0BLaK4EfF+iP8A/WMh/vwyL/ErityLiDR5SAmqWWT4GZQfyJoDp0U3DcQzjMMscg80YH6U5QBRRRQBRRRQBRRRQBRRRQBRRRQBRRRQBRRRQBRRRQBRRRQBRRRQBRRRQBRRRQBRRRQBRRRQBRRRQBRRRQBRRRQBRRRQBRRRQBRRRQBRRRQBRRRQBRRRQBRRRQBRRRQBRRRQBRRRQBRTdxPDbRGS4ljijHV3YKB+JrgXvGOk2+RA8l248IEyP944X+NASOiq8uuN7+5kMWnWsUTeWGnkx57VwB/GtVrHiLWBm8mmETeE8uxSPkT9RQE61DX9L09itzexCQdY0O9/91cmo7qHHkMYP2Ozdh07y4cRr+AGSf4Vo2PCUKSmO6uXdQoOyFREvMn4nw8xXct9JsLFC1raxI4/fxl/948/40BHX1bibV/7OJooj/2EYhX/AH35n8DSbbhO6uJTLf3aLJ0JGZXP+Nv5GprSI+r/ADUBxrfhvTbd03xNcsTzM7bwf8Pq/wAK7ARI4dkaqiAYCqMAVl/Xj+J+lZb1T8KAE9RfhXM0z/5xrP8AtY//AMS10e8SOJS7KowOprk6bOg1jV29PBePmEJ/1Y91AdiT2bfA1lfVHwpiS5h2MDIoOD63L605HIjKNrqeXgaAy3tE/Gl0hvaJ+NLoBEfV/mpm8toJonM0MUh2n10Bp6Pq/wA1E3sX+U0BoSaFpUnXT7UHzSMKfzFaM/DGlNNGogkUMDnbM/0zipBTMn9ph+DfpQEdl4K01+ayXCHwxsP1U03HwrPEWFnq9zCFOBjcP+FlqWUiP1pPm/QUBGRpXEVsCbfXHkx/2jN/5t1KR+MYcH7Vb3Ax09A/+Rakr+o3woT1F+FAR065xZAR3umW8i+YUZP5SH6UscYarEP9I0CY+ZXvB/5CP413pOqfN+hpdAcBe0G0j/tdhcxHyDJ/5itblvx1o8vrG5j+MW7/AISa6A5yv8o/WmJtPsp899Z28mfvxKf0oByLizRJOl8q/wC0jdP+ICtyHW9KnOIdSsnPks6k/lmo/FoGlSxEmxhU7m9mNn7x8sUzc8K6U0bFYpUIHhMzfwYmgJpHIki7o3Vh5qc0qq+k4Jsd26K4uEfwOEP/AJc/xrB4av4CotdcuYwTgDLjw9zigLCoqArp/FEHK31lX/2jk/8AErVlbrjCBsF7e5IGeif/APNAT2ioKOIeKID/AKRpELj/ALtD+jtSv+m19F/adCnUDqwZx9Ux/GgJxRULTtC04ELPa3SN5Boz9WB/hW/Bxto0gy0lxH80DN/wg0BJaK4sXFOiS9NRhX/aZT/iArdg1bTrj2F/aS/JMrfQ0Bu0UAggEEEHxFFAFFFFAFFFFAFFFFAFFFFAFFFFAFFFFAFFFFAFFFFAFFFFAFFFFAFFFFAFFFFAFFFFAFFFJlljhjMkzrGi9WY4A/GgFUVH73i/SLbIina7cfu2y7wf8Xq/xqP3vHV3JJ3VjaQwsfV7wmVz8EXH1NAWBXP1DW9N04lby9hjcf6vduf/AHRk/wAKgEycSarGz3D3IiwSRI/cJjy2rzP4ituw4PVVBuboqDz2W6BB+JOc/wAKA6eocd28QP2K0llx/rJmESfHxP8AAVxn1/iLVh/oYdIz0+zQ7QR/tH5fliu/Z6Jp1nOphtYy4XIeT02/NsmuoehoCEw8L3966zX9yisRyZ2aeT8zjH8a69rwvp8Mi9+Jbo4z+2bl/ujA/MV3YvZJ8BQfbL8p/SgERwRW8BjgiSKMA4VFCj8hTieovwrLeqfhWI/Zr8BQDa/2t/8AZr9TS5vZtWv36C7baS52AYQZ8TSpGlaM4jCL/eOT+Q/nQGzTHfRxs4Zhnd0HM9B4VnuC3tZHf3A7R/CswIqbwihQG8B7hQDbSO7JsjI58i/Lw/OlNHIynvJT8EGB/OnH9eP4/oaU3qn4UA1BFGqqyoNxHXx/Oufpn/zvWPni/wDxiupF7NPgK5em/wDzzWPmiP8AkoDqSezb4GkdzGyjdGh5eKilyeo3wNCeovwoBhraISJtQL19U4+lL7gD1ZJR/jJ+tLb2ifjS6A1o45AX2zv63iAf0olWcRP+0jYYPVCP1p6Pq/zUTexf5TQCN046pG3wYj9KaeSQXERaFujeqwPlW3TMn9ph+DfpQB34HrRyj/AT9KQlxEC+5tvpfvAjwHnWzSI+r/N+goBBmiZG2yIeXgwpxPUX4UmVEZG3Kp5eIrS1GfTdL06W+1KW3tLSFQ0k0jBFXwGT7yQPeTQJZ0RvSetH836Gl1D4eN+E5mAOuQ2TqQSl9I9oxBBwwWbaSD5gYqUIm9FeK5dkYZUjawI884pklxa3Q6vtX+A/Wl1rKswlbEqnkPWT4+RpebgeETfiR/OhAWnsf8Tf8Rpc3sm+Fa9s8ohH7EkZPqsPM+dKlmPdtuilXl5A/Q0Bs0h/Xj+P6GkfaY/EsvzIR+lJM8LOmJUPP7w8qA2KQPbN8o/WlAgjIIPwpI9s3yj9aAXSIujfMaXSIujfMfrQBKqtGwdQwx0IzWhHpOnTW8RmsLSQlBzaFT4fCuhJ7NvgaTb+wj+UfSgOTccO6Uy5FoqHl6jsnj7iK15uENLk9UTp8JN3/Fmu/L6n4j60ugIi/BdtFIptbyeNmPUqvl/dApz/AKO6rDztteuAPulpFH/GR/CpO/rx/E/Sl0BFhb8WQELDqsb4GfSYHP8AvRn60tb/AIwg6w29xjxKpz/zLUj/ANd/hpdARteJ+IYSRc6Mr4692jj6FqWOOpov7Zos8I8fTYf8SLXeT2knxH0pdAcnS+O9N1DU4LBYbqO4mOFyFK/mG/SpZVL6QO87WF91zL/AtV0UAUUUUAUUUUAUUUUAUUUUAUUUUAUUUUAUUVXHEeo6rpWo8ayHVLiRIdJtrm3VFRFtN0lwpZAeWQqKSzk5I8FwoEpZWfW+Cx6KqTTY5zqltwxqdzqdkj3e+dYdfuLkyA27OiJdMEmXJRmKAj1eXokgyrS+KIdL7O4Nc1iWe4giVgJYkMsk6CQrG4A9YsoVs+/NSYp5JjRVRjtq0vULhLfSwtvLIwSP7fFJGzE9BtKjn/ireaTiTWPWa7ER8z9mQfgMMR+dQSWDqGrafp39tvIYWxnYzekfgvU1Hb7jm0jDCxtZ7gjo8n7JP4+l/lrjWXCDh8XN0kWRkrbpz/3m6/lXctOHtMtiG+zLNIP35j3hz58+Q/CgODJxPruqkrYDYmf/AKSHd+Bdsj6U1/0c1S+ZZdRmVTnAa4kM7jn5ZwPwNTWEAR4AwASMfjWZfVHzD60BwbXhSyjwbmSe5byZtq/kuP4k117O1t7QvHawRQpgejGoUePlW1SF9q/wH60Bi49hJ8p+lKj9mnwFYm5xP8ppCSokEZd1XKjqaAWfbD5T+lLrWMpaQGKNjyPreiPDzpeyZ/XkCDyQfqaAVGwWBCxAG0cyaaM6tIpiDSciPRHLw8TyrMEEexWKhmx1bnTre1T4H9KAbPfuDnZGPd6RrEcCMimTc/IcmOR+XSnz0pMXsk+UUA2oC3RAAA7sch8TTk3sm+FI/wDrP/0f60qcgQtkgcvGgHKRH60nzfoKR34b2SPJ7wMD8zSFWZ2fLiMZ5hRk9B4n+VAOykKUJIAB6n4GkG4VgRGGk96jl+fSsGBA6E5ck8yxz4Gnz0oBiMTMi4KRrgdBuNczTos65qw7yTIMRznr6FdiL2SfKK5mnf8Az7V//wBD/wAJoDeeKQI2J3PL94A/pWVWcKMPG3LxUj9adf1G+FCeovwoBhmnEiZjjPXo5/lS+9kHrQP+BB/Wlv7RPxpdAa0c6gvuSQel9wn6US3MJicd4AcH1uX1p6Pq/wA36UTexf5TQAsiN6rqfgaRJ/aYfg36UpoYm9aND8VFMPbxC4iCrtBDeqSPLyoDbpEfV/m/QUjuAPVklH+LP1pCRyAvtmb1v3lB8KAfk9m3wNQXti4d1LiPhK3h0Zibq0u47vugQDKFDDbzOORYNz+751NJBOEb042GPukfrWVacKMxIeXg/wDyrGUeaLizbQrOhVjVistPOux5NeDivQtSn1DUba5SWdRBHPe2zA7PFFLAdSSSB1zV7dhenappnBLxavG0CyXcstrAVK91C230Qp9Ub95A8iPOp08rhk3QSDn4EHwPvpf2hB6yyL8UNaaVv7OWeZstL/i6vaKp+yjF5y2vjoLX2r/AfrS61luIe9bMijkOpxT6ureqyn4Gugphu09gPifqaXN7Jqat3WO03yMFRdxZmOABk8zWtp+r6brFtLLpOoWd9GjbXe1nWUKfIlScGgwdGm5FDOgIB69fhTlIf2ifjQCTbwk5MSZ89tNi3j71sb15D1XI8/fWzSF9q/wFAI7kj1ZpR+IP1FIjSXB2zD1j6yZ8fditmkReqfmP1NAMy9+InyYmG0+BH86InmWJAYlI2jo/8xTtx7CT5T9KVH7NfgKAYlmbaN0Mg5jyPj7jS/tCD1hIvxQ/ypcvRfmH1pdAa7XEJkT9qg69TinldW9VgfgaS4zIgPvrDQRN60SH4qKAV/rj8tLrWFvF3pwpX0R6rEeflS+4x6sso/xZ+tALT15Pj+gpdayRybn2zH1v3lB8B8KXicfvxN/hI/WgKy4Z9PtbYf8A3Vx/AOaumqV4NBbtV3Hr3s7H8Ub+dXVQBRRRQBRRRQBRRRQBRRRQBRRRQBRRRQBTJtbczyzmCLvpUEUkmwbnQEkKT1IG5sD+8fOnqQ00SzpC0iCZ1LLGWG5gMZIHiBkZ+IoDkLwnw4ujNpC6BpA0ln7xrIWUfcF/vGPbtzyHPHhXF7V4Uj7Pr6OJFSOIIFVRgKAQAAPAV2bbi7hu5jvntuINHmSwXddtHexsLcZIzIQ3oDIPXHSuN2j3lrqXZnqN5p9zBdWssaPFNBIHRxvXmrDkR8KZyDzW7bLixk+5e2z/AJTIf0r1lXki/O23D/ckRvycH9K9b0Ag+2Hyn9KXTbHEqk/dP6Uk3EecJmQ+SDP8elALi9U/MfrRN6n4j60zGZmB2hUGTzbmfyH86JIfQJkkdz5E4H5CgHHnjQ7SwLfdHM/kKbDyNIe7jxkD1zjz8KfRFQYRQo8gMVge2PyigGnidkbvJWPLonoj+f8AGs2kaLDGyoAxUEnHM8qeb1T8Kbtf7LD8g+lAKb2qfA/pS6Q3tU+B/SiSVI/XcL5ZPWgCH2S/Chvap8D+lMxyOUAjiJ/vMcD+dDJIzr3kmM55IMY/GgH3dIxl2VR7zTEcrGNRHE7EADJ9Efxp2OGNDlVG77x5n86zD7JPhQGvtle6G9wnofufHzNLeCNY3bbubB9Jjk/xpR/ta/7M/UUub2T/ACmgF0hPXk+P6ClCmTMiSOCctnooyelAOSetH836GlHpWu7yuV2x7BnkXP6Cl9xu9rIz+7oPyFAYSeNY0Xdlto9FRk/kK5lhI/8AXuqkQuciHlkAj0T7660AAhTAAyAeVc2w/wCsGrfLD9GoDfef0TuilXl93P0rCXMQRdz7eX7wI+tPP6jfChPUX4UA33sbyJskRuvQg09TMsaNIm5Fbr1GaPs0PhGF+Xl9KAXH1f5v0om9i/ymmY4Bl9skq+l98n60SxyCJ8TsRg+so/lQGzTMn9ph+DfpRi4H70Tf4SP1pp2mFxFmNCcN6r/D3UBt0iPq/wA36UjvmHrQSD4YP60hLhAX3B19LxQ/yoDzxxhx3qrcWa5BeTavbra3UltZx2dwYEiRDtDlRjvC2N3p7lwcAVdHZjrF9r/Amk6jqybb6WNllO3bvKuyB8eG4KG5cufKla1wxw1rN59t1CxtprsDO/cUL4GBuAI3dAPSzXei+z2lkoTuoLWCPAAwqRoo/IAAVopwqRk3KWUWl5c2lWhThQpOM1u876dP5KM7U+NNStOPL7Tbg6lFptnHELeOyuGt+8ZkDNIzrhjjdtAzt9HmDU+7F+INS4i4Rln1cySTW93JbRzyqFeaMBWVmwAMjcVJA/d881BeM+0Dh/VJ7fUdT4Ou73h9W7tNV73uppFycbYxhthJJG9lB58s8qunQ109dHszoyQppzxLJAIV2oUYbgQPfnP41FNT9o25ZXY2XdS3VnCnGi41Oss6PBXHbjxNqWgjSLWwNzFaXryG6mtjtk2oFxGrY9HcWzkYPo8jXK7F+J73WeJ9Q0yaO6m0sWn2mM3jmZ4JA6qVEjZZgwbPpEkbeVWVNJw5xYLvTXuNN1UQsDLDHMsjRNzGTtOUPMjPI9a81a9D/UPFfEFnJosJKXbrbtI7b4IQf2RjYklWK4bcDnJrXWnKlNTcvd7HZwy2pX9vK1p0v+7fmzhYyuncujtn0nUdQ4DiXR4Wm7u7jluoFBbvYV3cio9Yb9hI8gfKq24Bu9afir/pJe5j0zS7K4N/cQRbd0KxkiPPRiGCkL4YPlV09lFxqV12eaLNrZdr5om3O/NnQOwjYnxJQKc+Oc1JNStob2wuLW6jWW3nQxSRt0ZW5EH4g1sdLnkqibXgcVO+VrQqWc6cZPLXN1XR4+WhSUHbPdQrBf3r6abKR172yjDG4t4yfW7z1ZGA5ldi/GrtYTiROcTdfAj+dVhZdiejw6os097NcWCMGFq8Sgtg52s/Qg9DhR8atVvap+NZUfa4ftDXxJWKlH9E21jXKwI3zDrEp+V/5ikLMwkfdDIOnTB/Wqx7WeP7rh7iOy0W1nksYntftc91FCsspBdlVIwwKr6jEkq3LGK3+x3jS54rGs2164uJNPeLZdd13RmjcNt3KOQcFGyRgHlgCslVg58mdTTLh9xG3V04+4+vxwWF9oT94SL8UP8AKkw3EO3HeoDk8iceNbFNxAGPmMjJ+tbDiE3DK1tKVIPoHofdTieqPhWveQRfZpm7tNwQkHaM9KWLaMDluX5XI/WgHJei/MKXWtJCRt2yyj0h4g/Wl93MOkwPzJn6YoBbe1T4H9KXWse/Eq+yY4PmPL40vfMOsIPyvn6gUAse1f4D9aXWssxEj7oZByHgD9DS/tEf729fmQj9KAXH1f5qXWvFPCS2JUzu6bhT4IIyCD8KAq7gMd52llx4d63+U/zq6Kpnsz9Pj2Z/KJz9KuagCiiigCiiigCiiigCiiigCiiigCiiigCojqOk932jWOq2tnI0z6VeRS3IUtg77bu49xOAOTkLkDO89SxqXUU/39VglPBS+jR6tbaTY2jniDV9I0v7HNdLfaOLaSOSOQZWCJY1aVQBvOO9PoDa7k12OIEupezDiq6ht5Ldby6e5tYLuNoWWMugyyEbl3FWfBAI38wDkVaFR7tCTvOCtXX/ALgn8iDUp7+P3x+Fj7mLWfXn+WeQdQn1EWNx9ps7dUCEmSK4LYwM5wVFew8Tv1ZIx/d9I/mf5V5G4hbboGpN922kP+U16/qCTXMCd4u/Mmc+uc/w6U+AAMAYFJb2ifjS6ARH+/8AMaJvZtRH1f5qbnmjCsu4FsdBzNAP0j/Xf4aRvlf1Iwo83P6Ckd0WkxLIzcv3fRH8KAdkmjjOHYA+XU/lTFrJIbaERxdEA3OcDpWxHGkYwihfgKRZ/wBli+UUAho3Z1EshOc8k9H/AJ07HFHH6iAHz8TWX9on40ugEQ+zFDe0T8aIfZj4n603LKiyKN2WGfRXmfyoB+kQ+yX4U3vlf1Iwg83P6CsRQ74x3jsw+7nA/hQCZJkS8Xnk7CMKMnqPAUqR5XRtsexcHm55/kKAipdRhFCju25AY8Vp2X2b/A0A2INwHeyO/uzgfkKVEqozqihQCOQHupxfVFJT2j/h9KAJOqfNS6andU2FmAG7xrHfM/somI+83oj+f8KAXD7JPgK5lh/1h1X/AGcH0at2KN3jXfKwXHqpy/j1rnWVvEdf1NTGpAjgIyM/foDst6p+FYj9mvwFNNbxhTt3ry/dcj9axHC2xds0g5DyP1FAOv7RPx+lLrWZZg6YlU8z6ye73Gl5uB+7E3+Ij9KAXH1f5v0om9i/ymmUkkBfMLH0v3WB8KJZx3ThkkXkeqE/SgNmmZP7TD8G/Sj7TD4yKPm5fWkl1e5h2Mrcm6HPlQGxSI+r/NS6RH1f5qAJgDE+QDyNc7XdGt9Z0PUNNlAjW8tpLdpFUblDqVJHvGa6Mvsn+BpQ6ChKeHlHm1OxniO6uv6tvJkhsWwjXIn3psH3U9YkAcgQBkDmKlXahrkOm8O3nA3DbzCa0sYYZpHmVVhhwuIhyLO7RjGBgYbOfCrmf14/ifpXmDtkOit2oa69+97apDDAJTbqrvPMYlwRuBAUKYxjxIPMVxTpq3g+Tr3Z6S3vKnF7mP6pZUFnEYrpjdaZ8dTi2fEGqWOq6BfiOPZpt5FHEtvEEIUnDQg8gAyhhgkedXhoXGNhxHxJaaZrejaYNSZGls5VlW5Q7ebIHKBlcDJxjGAcE1WPDtlYXPCmn8I60kVpdahfi6t76CcTKt0VKIksfIpuTCeizjdzyOlWD2cdk7cOcQw6zqdzBJcWwcQR25YgFlKliSB+6zDGPHryrGiqkWorVPd9jo4nKyrxnVl/1zjlRik/eXR/HqWdaySC3T9ixGOqsP1pUs/oelHKvMfu58fdS7P+yxfLS5fU/EfWu88kMT39rbwSTXM6QQxqXeSU7FRQMkknoAPGoba9puhXV1av3V/Dp1xIIoNQmhCwSMxAXlneoJ6M6qvvrp9p+g3XE3Aer6RYSFLm4jXZg43bXVimeg3BSvPlz515n1ng7iK00K+e80zUo7e2RVl3gqgG4Llc+sASPVBwBmuavWlTa5Y5LrhfDqF5CTq1VFrZdWeneL+DdI4rSH+s45FnhBEc8LbXUHqOYII5eIOPDrWxwpw3pvDFnLaaVEyK7BpHdtzyNjGSf0GB7qobhDjTUBxZocNk2qzC6u47e8jurgypKjnaZAv+rK53YTauBgivRiwDe+2SVeY/ez4e+sqUqdV+0gtTVxChe2MVa3DajulnT5GzSIfZj8aR3co9Wdj8yg/TFIiE4jGGjYe8EfrW8qhd5/ZJvkP0p6tS6ab7NIGjTG081f8A5U73zD1oJB8MH9aAXJ1T5qXWs9wmUyHX0vFCPD4U4LiEnAlTPluoBR9svyn9KXTYIMowQfR8KcoBC+0f8KXSE9pJ+H0pdANooYNuAPpHrWDbwnmYkz57aVF6p+Y/WlMdqk+QzQFY9kvp8Y3LeVux/ioq5aprsaGeKrzPhaN/xpVy0AUUUUAUUUUAUUUUAUUUUAUUUUAUUUUAVyf+kFgeJk0FGle/Nu9ydsZ7tFUoCpfpu/aKdvXBBOARnrVxdQ0me54p0/UUlWOC3sbq2fB/aBpWhKleRHLum6+7kaLf5/x+SVjqaNzxtpsdxq1vbw3l3cadLDbtHBGCZ5ZSVWOMsQCQQQSSFUg5Iw2E6xqces8C6tMkE9tIkUsU1vPt7yF16q20sufeCQQQQSKjtp2e6ppE91Np2tzah3Ys3s4dRMSBmhd2YSNFCpGQ5Af0jliWDYFduTSru14J4kbVDCt/fpc3U62rsyRkx7VVGIBOFRRuwMkE4GcVKxrn1t/v5L446+vj/r6nlzX136FqKjxtpB/lNettOkE2n20g6PErfmBXj++06dLK426ldsndtmOQRsGGOmduf416v4YjWbhvSZJWaTfaRNhjy5oPCoJOjJMneKFO9hnIXmazumf1UWMebnJ/IfzpZUK0YUADPQfA05QGskO5n712bn0zgHkPAU46KkDhFCjaeQGKUnryfH9BRL7J/gaAXSD7YfKf0pQ6CmZJUSYZOTgjA5nw8BQD9M2f9mj+FG+V/UjCjzc/oKZtYd8C947sOfog4HX3UA7LKiyIN2WGfRXmfyo3zP6kYQebn9BStixtGEUKM9AMeBp2gNaOHev7R2YZPog4HX3U5sVGjCKFGTyAx4UqL1T8x+pof14/j+hoBdIh9mKUSFBLEADxNa8cw2ARo0h9w5fmeVALf+1xfI31WlzMFiYsQBjxrWdZXuY9zCP0W9TmfDxNOmCNVZsbmwfSY5NACzFlAijZ/eeQ/M0lUkd23vs6ZCfzNPp6i/CsL7R/woBvuUjKlV9LcMseZP40/SJP3PmFKZgoyxAHmaATD7JPhXNsv+sOp/7GA/8AHW5HNmNRGjOcdeg/M1z7QTf9INRwYwxhgJGCfGTxoDsN6p+FYj9mvwFNM04U5jjb4Of5ViOVxGu6CToOYwf1oB1/aR/E/Sl1rPcJvTcHXmeqEeFOC4hJwJUz5bqAVH1f5v0FE3sX+U1iIgl8c/S/QVmb2L/KaAVWtLDG1zEGjQghuqj3VtUzJ/aoflb9KAPs0Q9UMvysR9KRHCcvtmlX0vMH6itmkR9X+agGpUmEb4mBGD6yfyNZH2gAcom/Ej+dOS+yf5TSh0FAa7ySh03QnqfVYHw9+Kh3HnAGi8Ybpr6K6tb/AGBVuIRnO3mu5eYYA/A45Zqbv7SP4n6VpQ61pc+qSabDqVlJqMYy9qk6GVR70zkflWMoxksSN1CtUoS56TafgVBwj2RppvElrf6rf2zQWU6zxJEGDSMp3KW3AbcMAcc+mPfV2LIj+o6t8DmuLxNxLp/DcKS6gZXluJBDb28Cb5ZnxnCjp0HMkgDxIrX4Z4n0viSe6tYoJba/tgrTWl1GodVbowKllZTjqrHHjisKdOFJcsDpvby6v5KvcPOFjOOnwIP2m8f3XD2s6botrPJYxPZi7nuooVllILFVRAwKr6jEkq3LGKi3BXa3qtvrd5DxHepqWgrLGv214UguIA59FmVQFZBtIbAyMgjlyq2uIeCtG4psrU6jFIk8aYSeFtrqDgkcwQR8QarWPsNkfVMajqNvLpu9dzRqwlkXIyu3ouR45PwrTU9up5jqiys1wqpa8tduNRLfGU/LHXzL2rT1OS0itZX1N7dLIRMJjcECPYcA7s8sfGnu7mHSbPzID9MV5+7deKZrji6y0e3MOzRmE0wkGVknkQMh2HrsXnnPV/dz31aipx5mVVhZzva6ow0b69h/i7iDh3hniayj4Q+yW8U1sbqXVLLbduMsyCOEsWSP1X3HaeRAxU57HeNLnipdZtb1/tEunvEUuu67ozRyBtu5RyDgo2SMA8sAVWHZxwnNxzxDqep6zGzWawdzJcWu2NmuNylTkghiE3Zznky+Yqz7q/0Tsw023sdPsJZLzUJiIo5JVUysqjc8kh5KqjGcA43cl5muejKbfPtAuOI0benD9M8zuFjXOV33320LHpEPsl+FU5qnbJLHeRabFZ2NhelTLLdTTG5thHyAMYXY0hJyCG2Yx41LezDjhOLIdRtp1gW9050V3t2JimRwSjrnmudrArzxjqa6FVg3yp6lNUsbinT9rODUe5M7v+zSfCnqZu/7O/4fWnq2HIIk9aP5v0NKIBGCAfjSX9eP4/oaXQGubeEzc4k9XypX2dB6pdfg5H60v/XH5aXQGskTb32zSDn7j4e8UvZOOkqH5k/kaWnrSfN+gpdAa0RnCerG3M/vEePwNJupZVtZi0J5ITlWB8PwrYh9mPifrTGqHbpt2fKFz/lNAV/2OL/8T6ifK3Yf51q4KqXsaXOu6q/lHj82/wCVW1QBRRRQBRRRQBRRRQBRRRQBRRRQBRRRQBRRUf13Wb7T+IdAsoLKJrK/uWgmuZJMFT3MsgCKOp/ZcycAAjG7J2lroMbkgrncSjdw5qo87SUf5DUO1ji3W9D1e/ttQTT5wbWa4tIo4JYQhVlEatO5xMWDZYRoCmOecqT1rS91Gez1/Sdbls57+1tw/fWkDQxyRyI230GdyCCrj1jnAPLOKLVZD0PMd0u6GZfNSP4V6V4EfvOB+Hn+9p1uf/1S15nF1bXLOILiGXmR6DhvpXo7s5uY/wD2ecLFmyzaVanA5n2K+FASST1o/m/Q0utZ3kcrtj2jPIv/ACpXclvayM3uHoj+FABmRJHDN6RIwAMnp5Vh3ldG2x7Vx1c8/wAhS4kVHdUUKOXIClv6jfCgGlhLqDLI7DHQeiP4UpUWORAihRg9B8KWnqL8Kw3tU+BoBdM2nsB8W+pp6tS3nRY9oy7Bm9FRn94/lQGw/rR/N+hpXTrWu5mcp6IjGeRJyfy6UsW6nnIWkP8AePL8ulAJSdQCEDSNk8lHv8+lYfvnZM7Yxnljmeh/CnYhhSB03GsyetH836GgEC3TIL5kYeLnNLh9mPifrS6RF6n4n60Ah/7VF8rfpTj+o3wrXnlRLmLJyQG5LzPh4UtmmdTtQIuOrnJ/IfzoB1PUX4Uz3694+wGQ8uSc/wCPShIFZVMpaTl0Y8vypxABIwAAGByFANP3z7c7YxkdOZ/lS1t4wdzAu3m5z/6UuXovzCl0AiH2S/Cufa8uItR/8PAf4y1vxECIEnAA8a5dvPGOIL87sqbeDBAJHrS0B126GkxezT4CkC4hYECVM+W6lxc4kx5CgB/Xj+J+lKZQwwwBHvFJf14/ifpS6A10t4Sz/s1B3eAx4ViWBRE5VpByP75p6P1pPm/QUTexf5TQCO6kHqzv/iAP6U04mFzF6UbHa2PRI8vfW3TMn9qh+Vv0oA3zjrEh+V/5ikRzEb90Mg9LwAP0NbNIj6v81ANS3EfdODuU4PrKRS0nib1ZUPwYUqb2T/KayyK49NVb4jNAcziaK9uNB1CHSZO71GS1mS2kzjbKUIQ58MNivLdlY8T3JsuH9PtO5vbSVJIE+zlJLeUMCJScZXnzLHwzXrBreHvExGq5z6vL6UvuAPVklX/GT9a0VaPtGnzYwWfD+JKzjOLpqfN36Fedr/BF5xbFYXWlShb3T2kCxl9m9ZFXdg/e9AdcDBPOuf2P9n2p8Oaxc61rblLh7Y2kcBlEjBS6sSxGR1RcYJ6npVoJHKHfbMev7yg+HuxSz9oA6xN+BX+dS6EXU9p1MY8UrxtHZLHI/BZ77hZ/2SH5B9KXL6o+YfWopJx3w9YwxxPqtlPOuIvs9nMLictjp3UeXz5jHKuro+v6frtgLvS5vtEAk2MVHNHGMqy9VYZHokA8+lbco4HFpZaKf7U+1i50bjm+0CK/uNJtbGKPM1tbRzTTyugfrIrKEUMvLbknPMCo72d2X/tgudYuNUukg1jT2ijmvY7YBLyMhgjtHkbZMJgkHGNvo8jm3uOOzvhjjK9S91VJ7e9VQhngPds6joGDKQcZ64z78V1+CuFtE4RsTY6DGEjf05ZGfe8rchlj+gwPdzq0uXw6rZRpxg/a6Zzt8OplaXVxaVva0Zcr8Da4O4aseFNGXTtNDFC5lkkfG6RzjLHHLoAPgBXA7TuA4+NrS2KTrBfWTuYWcEoyuF3KcdMlVOeeMdOdTukR9X+b9BVS6cXHka0NtO8rU6/6mMvfznPiUlpnYTH9leXUdTWPUMbY+4jMkSDPPOdpbOB93GPHNWJwFwTpvCenSx2w7+4uSrzzSKAWwOQA8AMnA59TzqVnpSYfZJ8orCnb06bzFanTd8XvLyLhWqNxbzjpn4GvdW8SwkqgU5Hq8vEU73GPVklX/Fn65ou/Y/4l/wCIU9W4rTWaOUOmJieZ9ZQfD3Ypf+kDxib8Cv8AOlv7RPxpdAaweUSnMQJ2j1X/AJ4pffketDKPwB+hpY9s3yj9aXQGslxGC+4lfS/eUjwp1Zom9WRD8GFZj6v81ZZEf1lVviM0BiH2YrV1s40a/PlbyH/KacitoTGp7sA4/d5fStPiCEJoWpMryDFtIcbyR6p86AivYuM6hq7e5R/E1atVZ2Jc5NZb/Zfx3fyq06AKKKKAKKKKAKKKKAKKKKAKKKKAKKKKAK0dS0uHULrTLiZpFfT7g3MQQgBmMTx4bl0xI3THMCt6igIpc8EWl7cTtqep6rfW7JKkFtcSoVte89Zo3CCTdjkCzttBwMVu6ZoS6TYakZL+91K8uwWmurwp3j4Taq4jVEAAHQKOpJySTXepMq7onXzBFFoDxrqGmWM91KZ7O2lIc83iUnOfhXorsnwezHhQgAH+q7YHAxkiJR+lUDd/2qb52+tXz2QNu7MuHR921VP90kfpQEuk/d+YUukS9F+YViSaOM4ZhnyHM/lQGV9q/wAB+tKb1T8K1w8jyN3abcgc35efh/6UowlvayM3uHoigATxqiqWy2B6K8z+VJZpXddqCPrgvzP5CnYFCxJtAGQDyFZf2kfxP0oBHcBvau0nuPIfkKxaACIgAAB3GB8xp+mbX1H/ANo31NALk6p81LpuYhQpYgAN1NJ7/d7FGf39B+Z/SgFxfvfMaTO6psLMBzptEkfdvk2jPMJ/Old0kZUqvPcMk8yfxoA7139lGcfef0R+XWkxwl1/aSMRk+ivIdfzrZpEXqn5j9aAaKJHPCEUKPS6Cn29U/Cmpf7RB/i+lLldI1y7BR7zQGY/Zr8BWF9q/wAB+tNRySMiiOM9PWfkP51gRF5GErluQ5L6I8aAVPMgIXOXBB2jmaMzP0VYl825n8ulKZFRFCKFG4cgPfTtAa8UCFQz5c/3jkD8Ola0H/WG9/8AC2//ABzVvQ+zFc+H/rJd/wDhIf8AjloDouoYHcAfiKZjt4TGh7tQcDmBinz0pMXsk+UUAy8Ch02vIvP75Ph76X3cg9Wdj8yg/wAqW/rx/E/Q0ugNZO/BfBib0vIjwHxoleURPuhHqnmr5+uKej9aT5v0FE3sX+U0Ajv8etFKv+HP0zTT3EX2mIl9oCt6w2+XnW3TMn9qh+Vv0oBayI/qOrfA5oj/AH/mNYaGJ/WjQ/FRTUdvH6WAy+l+6xH0oB6b2L/KaXWtLCRE+2aQcjyJB+opeycdJUPzJ/I0AtvaJ+NLrWYziRMpG3XoxH6UvvXHrQP+BB/WgKb7Qu0i803jXUNGgvZtMtbJY8y29ukss0joH6uGUIAy8tuSc8xW1Fr2s9oPYvr/ANiUDV4pGs3aBCguEUo7lVySC0TEbefPI91SvivgjQuJ777XqMd1BdgBDNB6JZQOQbII8euM++tu4u+H+z/g26nXbb6ZYxmRlQ7ndienM82ZiAMnxA5CtEadWVRpvR7Y3LedxYwt6bpQftU03n/HT66nmu0teJNR1YS6fBdGW1thaiOytie4QEnbtAO3OfLwrvcMcb3XZ1qXEEOq2rXmq3AtppLa5uRAVwDjlhmMjB15bRgKCSKs/hztXtbrVdL03VLGOyXUHWC3livFnKyEeikyhRsZug2lxnkSKo/XP690aG90fXY4xcXE7PP3kOXuZixPeKcZck+qRn3Vrq28rCSlVTbe35Lqhd/+bjK3jCFOKw33xnXDZcHD/a1NNr+l2eptpdxBqM622LISK9rI5wgJYkSqSQpYBMdcGt/iDtUsrXXdRsdP06G/TTnMFzJNdLAXkHNkhUqd7L0O4oM8smq/0O24O4T0leJdY1q2vtX05EnXR9v2aVbjkApST9oQHYENtHTdgjlVYcd2Nnc63c6s86Jd6jK91PZfZ5YXheQlgV7wZdCxxuwBk9MVacJjQqSf/kJcke6Ta+OCk4jbUZVVHh2ZLx0efBeR680vibh6/wCFLTiMXsFlpNygZZrmUQBDkgqxJwGBBB59QcZryxxzxdfahxfxCCtvqSPdyRWF6JjMttADtjaAgkKcAMWXmT1rS4la4sdO4W+w6np95DpCtHFZrExWGWR2dpDuJDks3rYUDavLxrhtrk9xp94L/SYLnUrp2ll1GTPfiTw2t4AchtHIjrV7wjh8LuFWdtieVJLLw49pfw/HYra1KpZ1YK5g1s8d1nYtPQ+0DVNJ1fSHsJ9du1MyQXcN7dtdC5jY4LBXbCOM5G0qOWDyqep232jWr39ppgn0eIkGRrlYrmRV5M6QkEFR73UnB5VTen8K6/x2002gRxRy2kdubm1guAqozofTUtjAJV8rk4OQOWKlWm/0b9TcWn2zVbGKJlzNs3u0fuAwA3L3j9a4uGcOslQ9pe3Ky+iTeMdH6x5nZxmtSlX5bai4JLVPfO56Nhvkv9Ntry1AltbhY5opEbIdGIKkZx1BFbnfgetHKv8Agz9M1p2OnwaRoun6bZhha2aQ28QY5IRNqrk/ACulVO8Z0K81muIu8TLhevrcvrTyyI/qurfA5ob2qfA/pWGhif1o0PxUVAMr7V/gP1pday28fePgMvIeqxH0pfckerNKPxB+ooBcX73zGl1rRpMAdsqn0j6yfyIpRM4HqxN/iI/Q0A5D7JPgK5/Epxw9qXvt3H5qa24pJBGmYGIwOakGubxPODoF8Ckikxkc1OPzoCPdh4/Z6yfMw/8Anq0arPsRXFnqreckY/g1WZQBRRRQBRRRQBRRRQBRRRQBRRRQBRRRQBUR7S7Yy6Tp8/2i5j7jVLAiOKQork3cK+njmwALeiTt55IJCkS6ipTw0+zJTwVRqM/DF92jzxaLc6Xb8UWTSNNObpBe3MxgIW2RSd7RgEO37gKgAE7im12Wto51KJeF/s32caZGdV7gc/tm4Y749e/x3u/d6fq7vCrNoqI+768/z9ERL3vXin682eL7/UJ4b64WfS71MSN6SbHHX+62f4V6A7HJZG7NtFWOPO1ZF3McDlK4+PhVLayuzVrxfKVh/Grq7FDns20z3S3S/lcyigJhJG7KDLISMj0VG0dfzp6ONIxhFC/AdaJfU/EfWl0Age2Pyj9aXSP9cflpLzxodpOW+6oyfyoBUPsk+Aof14/ifoaZjMzRqEVUH3m5n8qGhBZO9ZpMnnu6dD4dKAWbhM4jzI3knP8Aj0pm3Ezh/SEY3t0GT1/KtsAAYAwKatv9b/tDQCWhRSrHLNuHpMcmtikS9F+YfWl0AiPq/wA1Ev7vzCm++RHdSctu9VRk9B4UmRpXAwgjXI5scn8qA2CQBk8hWuk4wRGrSHcfV6dfPpSxbqTmUmQ/3un5dKVF0b5jQGvKsrzQ72CAk8k5np5n+VPpCiZKr6X3jzP51ib20HzH6GnqARF7JPlFA9s3yj9axGyrAhYhQFHMnFNCYvITChfIAyeQ8aAel9UfMPrWJJkQ7Sct90cz+VNSRyMAZZOWR6K8h1/Ono40jGEUKPdQDMZmdAECov3m5n8q0Ioc8R3IMkhP2SI53Y/fk8q6sPsx+P1rnR/9Z7n32cX/AByUBumKQD0Z3/xAH9KTEJxEmGjYYHVSP1rZpEPsU+UUAy7zB03RKef7r58PeBS+/wAetFKv+HP0pb+vH8f0NLoDWS5iDPufb6X7w2+A86ceRHhfY6t6J6HPhSo/Wk+b9BSLiKNonLRoTg9RQD1Myf2qH5W/Sj7NGPVDL8rEU08TC5iCyyD0W64PlQG3SI/3/mNI2zjpIjfFP+dIjacbv2aN6R6Nj9KAem9i/wADS61pZW7pg0Mg5deR+hpf2mMesWX5lIoBbe0T8a19V1Gz0nT5r7U7qG0s4RukmmcKqjOOZPvIHvJpzvonkTZIjdejCoD268M6vxRwVFBw+x+3Wl5HeCIEAyhQw2jPLILBsH7vnit1vTjVqxpylypvGexDeFk6emdpHCl/riaTFqvc6jOVMUN3bTWxkzgLtMiKGz4AdfCupxzw5bcWcKajol67Rw3SAb1GSjKwZWx44ZQceNeULXs97QOKNas7e9g1OExv/arqJo1hBIJbcQM4wGwMnlyr2XJ7Nvga7+IWceH1Y+yqqT3ynnGNjGEudaooHgLsDfSeJ7HVdX1CCW2s5kuYY4N26RlO5d2QNuCAcDOcY99Mdvd1qLdo+haZYXUcEcFg13G00+xInZ2RnY8z0VQMAnmceNaXbLrd/YcZ3a6rYR3+mxW8AsLe5JMWGUbnCdNxcsu/GQF5VXHHyfa7TS7u91WLVJreP7MwQuZIYyzOqbmJ7xVLsAxweg6YrUr+PGb2NPiNRpf45x8tF4l1S4ddWVKN3QinlZXXC7vp8zR12TU9Qvp3lvG+2acVMv7QOrBcsrAjkyjqCRTeoWuuXF9pc/ED3skPeHYzx89vIsASMc+RGfiKd4Ru3mttV4a06C8kg1uD/SUVI8q8LCSFgWIAG4FWJYDDnkSBUp7NuB5NS1VtW4l1SO00TRLtXv1vJ8HeuCEKk9GJC56EE4J6V6KdlDh1pc2TqRS1ceaLctV38X0epxS4l+puqV1OGqxnleM4fbo8djlJLdrrGmNoFrI9+t0kluroCe8Vg0fuOWAHh1FWb/SZ+y2mocOXs2nXGJ3mS6lhwrOiBCse7njJY8xg4Bx7u7bcd8C8L2V5qvDPDupXttDlXvoIByPioMziTaDjJVSorgdo/a3Y3PDjaZqWh2E1zeSK1vKJxeW0Yz6T5ARxIoJwAMHPJiOR8vwbh9SlVj7Snzxb1S0yd/GuMq9qqpRzHlW7eWNf0cOIIZeLdesdPsZLXS7izW5JnYu0UiMFCBzzKkSEgMSRg4r0VFIjIu11PLwNecuw7jWwtOLrbhrR1NxY6lHIWmmtljnjljRnG51ADoVDAAgkE9fP0Z3MboN8aNy8QK6eL0I0LlxhT9mtMJlKqkqnvTll9zF16qf7RfrT1alxbxgR7VK5cD0SRXA4r4r07hq4tbSeS9uNQugzQ2dsFaRlX1mJchVUZ6swz4ZqujFyeIokk7e1T4H9KXUa4U4ls+J4ZpdMncS2zmG4t7mHZLA/I7WAOOnQgkHwJrv5nH7kbfBiP0qJRcXhgWvtH/Cl1rLK4d90L+HqkHw+NL+0IPWWRfihqALi9U/MfrSm9U/CmIbiHbjvUByeROD1p5iDGxByMUAR+zX4CuRxi23hq+P90D/MK66eovwrh8ctt4Vvz7k/41oDmdia40jUG85gP8tWPVfdi4/+HrtvO5I/yirBoArnQ65pM+qyaXBqljJqcQy9olwhmQe9Acj8qxxNDfXHDerQaPJ3WpyWkqWsmcbJShCHPhhsV5F0/T+KrmWx4e06zMF/aTJJAn2cpJbShgRKTjK8+ZY+Ga0Va3smljOS04fwx3sJyU1Hl7vB7Mrm6brmnalPqMNlciWTT5TDcjYw2OBkjmPS8sjIyCOoIpHFWrf1Hw9e6gqd7LEmIYv+1lYhY0/xOVX8arTQbHW+D9c0eTW7DTLe21C1OlXVzaX0lw09zl5Y5HVoYwuXacZBbnIB5Vtbxn1r60+KKzGmfXj+fgWtpd/barplpqFhJ3tpdRLNDJtK7kYZBwQCOR8RWItRtZdVuNNjlze28Uc8se0+ijlwpzjByY36Hw+FUVw/qOlx2+k2/EnEuo6TYx8K6bLaxQ6hLao05EoJXYw3yYUYj57sc1baMbmqjVZ7PX9Z1K61Cw12x4TsbxhbzvblbofaWy6qQGwQcxsCvM5BrdKGJNLo/wA/j+PhKjltddPrj8l6UVSPG/Ewt+Nd1pqV3DdWWoWEdzHPrEkPdwM0XeNHZIpSSErIQ0spGGJAPoqKu6ta1jzeun5MMhRRRQkKKKKAK0tW1aw0iO3fU7uG2W4njtYe8bBklc4VFHiSfAeRPQGt2o/xrpUmqabbC0tkmu4r20kDHaGWNbqGSTBPhtjyR47R1OKlatLxJWp0pNX0+PWU0l7yEak9u10Lbd6fdKwUuR4LkgZPXnjoa1eH+JdL4g73+qp5ZO7CtmS3khDo2drpvUb0ODh1ypxyNc/WtClu+Kra6toI44H029t55xtB72Q24TI6sdsbc/JQPKtPg2z1Z9StbnVdLk0xdP01dPAeeOT7Q+5SzrsY+gNg2ltrHccqvijrv63/AAvnkS0WV62/2/gUFxSmziPUl8rh/rVvdhrbuzWw8xdXo/8A8uaqY47tL9OM9aNvqChftcmEmgDBfSPL0Spq2ewVZn7Pkjlm5x3t0GEY2gkzMx65IHpVBBY1w6omGYAnoM9aT3sj+yjIH3n5fw60NEkcbFFAPiepP40/QGt3ReTEzluXRfRFPoixjCKFHkBWD7YfKaXQCIfZiiTqnzfoaxFyj5+/603JOrFRFmQhv3en59KA2K14nWPvi7BR3h6n3Cs7Zn9ZhGPJeZ/M/wAqRaxIskxxlg+Nx5noPGgMySs4HdxtjI9JuQ6/nSu5Z/ayEj7q+iP505L6n4j60ugGoUVN6oAAG6D4ClS9F+YfWhPXk+P6CkzsFQFiAMjr8aAdpEX73zGm+9d/ZRkj7z+iP50lIS+7vXJGearyH86AxcTIJ4QDuYMcqvM+qaX+3f7sS/7zfyH8axIio9uEUKN55Af3WrYoDXghTarkbmx1Y5x8PKnR7Y/KP1oh9kvwrBIWVixAAUcz8aAzL6g+YfUUutaSYOv7JS4yPS6L18/5Urunf2shx91OQ/PrQAsyIoUnLZPoqMnr5VzY3lPEs5EXM2cfJmwcb3rqW6qsfogDmenxrnp/1pm99mn/ABtQG/3zj1oJB7xg/rSIriMRIG3LgD1lIrZpEPsU+AoBszRO8eyRG5+B9xp+mpkV2j3Krc/EZ8DWPs0X7qbflJX6UAuP1pPm/QUTexf5TTKQkM+2WVfS88+A86JUmET4lVhg+sn8jQGzTL/2qL5W/SjM46pG3wYj9KaeVxcxFoXGFbpg+VAbdIj/AH/mNI+0xj1t6/MhFYhmjbdtkQ+kehoByb2T/Cl15W487UNVj404gtL6XWLdbS7ktrKOyuDAkKIdokKjHeFiN3p7lwcAVfnZRrt/xL2e6Lq2rpsv54mEvo7d5V2QPjw3BQ3Llz5cqsbrhdxa0YV6qxGW3yyYRmpPCJRIiPIm9VbkeozWPs0P7qbflJX6Utvap8DS6rjM4Ot63pegBDqV/JA87lYYkVppZSAM7I1DM2MjOAcU9o+rWmuaa15pGoRXduCyMQvNGA5qw5FWGRkEAjPSqv7ZuGOIbviS313QftMsSWv2R0t13PGdxYkL1O7cByH7nOut2L8N61o1pruoa8ZUl1ExFIpeTjYrZcjwJ3AYOD6HOtCqydTk5dO5aTsKcbJXSqrmf7c679vqd3tE4OPGvC8envKkE0TpPbzcztcDGCPEEE+PXB8Kp+x4W0vhriZLPimH+uryGPv207TY1dQpyFeV5GRR4kIPSJwenW69N494YvLy3sbfVoXllfuIpNjiGaTpsSUju3b+6rE1U/bJ2TcQa1xnda9w5MZU1ARCaETiJkdECDqQCuFB65yTyq2sbWhcVo07qSgllqTXXzOOnxC5tqUqVGbUZbpdSlLfQr7U5oH0zvmumQwMkCOruVY59HkevLGPAVatn2WaxovAWpXNzqUQ1R7q3vpoWnXCxQJIMM7ELkd4WPMjCDmat3sa4LueB+EXsL+5Fxe3Ny95OVJZVZgq4BPXkgJPmT8a2+1bQLzijgTWtI0xwl7cQoY8nG4rIHKZ8NwUrz5c+ddFe9q1Kb4bKqpUub/JrXGd29/Eyd1BV4XVKmoyWNP2trw6Z6o8b6bo1ze2dyum35ktYS0YBuBGJOWSqhiM5z5YyevOrk7GuxfR9Y0i01/WLqO/sbm3PcW8JZSreqSzcvSUhhgZGR1I6062kWun8R6lZcbNf2NzCcvHDEO8aRxu3HIIC4IPIc88iBXpv+jVdQ3vZjFa27SgadeXFr3mSBLl+9DBT05SgY8wa9Jxm6ure0j7Oba0TkopJ+Ulvqt1grY8s6jeMeHYkfBnZnw7wdczXulwzS3rIyCe4cMyKeoXAAHxxn31xu27tAuOCbfRLa0YW8mpPJvu+670wxxhd21TyLkuoBOQOeQai3b1xzqfDfFOm6UJNQGkPZ/aZDaSdy88hdlCGRcMFULnCkE7hmoxwHxZa9o+qjgri22uLy3lZ59Ku55f9IgZULNGzgekNoYhmyTgZzyxSUrK4rKPEL1OdPq85eNuvYzckvcjuTjsg7TbjiziW70O4nkvoY4BeQXcsKxSgBwrJIFAVubKQVVeWc1jt27MtZ4s1iz1vh2fNzFai0lt+97ssodnBUnAPNjkEjoOtTTg3gbR+CkI0izkM8zASXEkgeRwM4HQAD4AZ8egqYd+B60cq/4CfpXJK+p2t5+osFiK25kn0w8mXK5RxIrDsK7P9Q4JttTuNauBJqGpd3ujD7+7WMELlvFvTPTIwBzq1a1/tEPfDMij0f3uX1p5WVhlSD8DXDdXM7qrKtU3fwMopRWEYT15PiPpS6QnrSfN+gpdaCRuMBowCARk9fjSJbeHYx7pAcHmBinIfZiiX2T/ACmgG1t1Cja0i8vBzUf4/V4+Er8967D0OTAffX3VJh0qNdop/wDhO7HmV+oP6UAnsYH/AML3J/8Au2H+RKn1QXsbGOE5T53Tn/KtTqgCiufxDJexaBqcmkoJNSS1la1QjO6UIdgx82K84WzajCtteaQgbX96GO975jPcyZHoSNnLqxwCrEiuK6vqdrKMZ/u2K+94lSspRjUz72x6au7mCztZrm8mit7aFDJJLK4REUDJZieQAHia5Wi8WcOa7dNbaHr+kalcqhkaKzvY5nCggFiFYnGSOfvFc/tX/wD2Y8V//wAruf8A8bVG501604j4JfW7zStTiaWYQRWVjJayxN9lkPeEtNJvUAFSMLzdT4AV292yxa0TXj9Mfkn0GkwQa/eaujym5ureG2dSRsCxtIykDGc5lbPPwHTx6FUHc8Q8Sa7wNrLalJqNva6pw/eXuZ209REyKD3dsiM0rRkMyOZVLD0eaMa7naDxFqugaNIdI1vVZbnSNIjup44bWz25O7ZJcyS7QUYoVCQBX5MfFcTh9fW/4JcX68MfkuCikxP3kSPkHcoPLpSqgwTyshRRRQkKKKKAKKK4PHWsXug8KanqemWcd5c2sEkwSWTu41CIWLMeZxgdAMkkDkMsBMU5PCO9RUK17iPVbO/vprT7Cul6TDDNeJLE7zTh8lu7YOAm1Rnmr7jy9HGSrQeIdVudUspL/wCw/wBWapLcRWcUMTiaExFiO8cuQ+5UY8lXacD0utDHmW5RfHoxxprf/i5P+I1ZHYIc8HXi/d1GcfntP61XPaFJE3HOtrHIjMty+4KwODnxqwOwWRU4X1fewULqjjmfOGE/rQksyb2T/Cl1rSTF427uNiuDljyH/Old07+1kOPup6I/nQGZJUSZcnJwRgDJ8PCsbpn9RBGPN+Z/IfzrKxpHIgRQoweg+FPUBrRQKy5ky5yeTdOvlTsgwEx03CsxeqfmP1ol6L8woBdMwe1uPnH/AArS5JEjGXYDy99a0TyPLN3SYBYHL8sch4daA2ZvU/EfWkNOmSqZkYeCc/49KRJCShMrs58ug/L+dbCgKAFAAHgKA11Eru/pCIZ5gcz086U0KIAwGXyPSY5PWnE9o/4fSib1PxH1oBdIj6v81KJAGScD31rpNkv3SmTJ5EdPzoBc/tIP9p/5TSpJkjOGb0vBRzJ/CtedJHeHvXABf1U5Y5Hx61sxxpGMIoHw8aAZiMzxqFCxrj1m5n8qysK996ZMhAzludOw+yWj/Xf4aAJfU/EfWl03OQIySQBkdfjSO+L+xQv/AHjyX8/5UA5F6n4n61ye9jTimXc6j/Q1HM+O9uVdCOIyL+1ckZPoryHX860Y0VOKHVVAX7EvID++aA6qsrDKsCPcaxD7JPhSWghY5MSZ88U3FAvdKVaRTjwc/SgHn9aP5v0NLrWeOQNHtmY8/wB4A+B+FL/0geMTfgV/nQC4/Wk+b9BRN7F/lNMpJKGfMJPP91gfAeeKJZx3ThkkXkeqE/SgNmmX/tUXyt+lC3EJOO8QHyJwawxBuYiDkbW/SgH6aVEcNvVW9I9Rmnaq/Wu1i1sda1Kw02wjvV06Yw3Mkt4sBeQeskKlTvYdDuKDPLJrZTozqvEFkhtLck+v8CcM61d/btS0e2mu1A/aDKFsdN20gN5c8134LOO2gjhtS0MMahEjTG1VAwABjkAPCtHh3XbLibhu01jS3Z7O7j3puGGXngqR5ggg+8U7xPLfwcNatNo6d5qcdpM9qmM7pQhKDHj6WKmUqksU5t6aYfT8DTc2mSYSLiVTyPrJ/I0vM46pG3wYj9K8UaVxXr5vrD+qbBzxF36bL8Su1xcSFhlZGPN1bpsYke6vYXGnEEPCvC9/rNzE0yWqAiJTgu7MFRc+GWYDODjOa7eJcMq8NcVWxqsik/avlhudKOVwX3Qv63hg+HxrncVQNqnDGsadBK9tPd2c1vHKysNjOhUN+BOarfh3tYll1/TbPUm0y4g1KdbfFkHV7WR+SAliRKpOFLAJjOcGreuPYSfKfpVXTqKXvRex0XFrVt2o1Y4bPHun9n/aBqN5BoEgure1jZFMjYEMKqRhg45HHX0STXsOTrH836GtPUb7T9MsPtWrXVpaWqgBprmRY0B8Ms3Ki3NleW9vc2MkM1vL6SSwPlWGDzBU4NWnEeJTv3GU4KOOywcsIKBV/wDSF4y1Lha10KCwN1FaX0spu5rU7ZdqBcRq/wC5uLdRg4Xka4/YDx3qPEXFeqaY/wBuk0pbMXMZvJTM8EgcKUEjZZlYPnDEkbTjlVw65w/p2u2DWWqwC6tid2yX0sHzBPMHmeY5861eGuGNN4Zilt9BtYLWN9pf0CzPjONzE5OMnqfGsoXNorJ0XTftf/bOm/b6DllzZzoQP+kFwxw+3CmpcU31lI+pWcSIjwvt7ws4RA4IIIBcE9DgYyOWK77Le0qLQ9W4f0DS7hrvTr27W1nt3tVj7t5WwJInADYDEZDlzjoR4ekNUsU1TTriw1G1gurO4QxyxsxAZT9PjnIqEcJ9lnDPDesrqtpY3Ut1GxaHvpFdYTzHogYyfe2fPrW+2vrd2kqF25Sa/wAVn3Vp62IlF82Ykj484R0zjDRmtNUjIePLwXEYHeQt47SR0OMEdD8QCPGmi8QJw9dNqVrDf2ev2+7uZwVxA/MEFWByCMqQR0Y/Gvc0twndODvU4/eQiqG/pD8LtDd6RxLwvplrJLDNK980ce/LkKY5HQcuRDktjqRmt/Ab2MZO0raxnovews+PgzGrH9yLh4S12PiXhfQ9WjeBnuoY5ZVhcOschjyyZB6qSRg8+VSGvO39HiPiW/4v1HXNUiMWm3NuIpHCbFuJwco394hd4J94z1r0TVTf2rtK8qLaeO2qNkJcyyN9Zef3f1rDW8LHJiTPnilf64/LS64zI1kt0y+0uvpeDnypfdOPVnf/ABAH9KXH1f5qXQGtEJxGuGjYY8VI/WiV5hE+6JTy6q/8xT0Psk+FE3sm+FAI78j1opV/DP0qM9ok6PwzMqk5LDkVIPQ+dSyol2nHHDJ98oH+VqA3uyFdvB6n707n6VNaiHZSu3gy297uf41L6AK1Y9NsY7572OztkvHGHnWJRIw8i2MmtXirUJ9I4Y1jUrSD7Rc2dnNcRQ8/2johYLy58yAK8gWHbLxFBcWl5Bdazd6z3qNMks263uQSN0XceogI5Aoob31YWXCri/jKdGOVHcwnKMccx7Ou7aC8tZra8hiuLaZDHJFKgdHUjBVgeRBHga5eicK8PaDcPcaHoOk6bO67Hks7OOFmXOcEqASMgcqTxxf3OlcGa7f2Azd2tjNNDyz6aoSOXjzFQnUtK4c4W/qHU7TQb4zPPb79e04wCWR5ZFTFy7uJZVkLjdyfrnkQCK+P+WPJfM2Ne78/pgnttw7olrPfz22j6bDNqGftkkdqitc5znvCB6ecnrnqaZfhPh2RrRn0DSGNpEYLYmzjPcxkEFE9H0VwSMDlzNRA8banHxxa6b3+m3Wn3V3PaqlrY3JEPdxSOC12T3LvmMhogoKkkZO0k6micU8Z6rHoQEvD8L6zpDapGxspmFrs7rKsO+Hebu9GMFNv9+o6Z6f2/wCEyWnnBaMEMVvBHDBGkUMahEjRQqqoGAAB0AHhS6qW44/4kuNEudU06HSYYbPh601yaKeKSQyNIspaFWDrtH7MYchseKnPLsy8T67Yya/aalcaFHc2tra3VtcPFLHFH37yJ3bqHZpWXu+W0qZCQoC5zWcouLeenr1/RjjHry/KLBoqI9nHEd7xDaasNRCNNYXptRKtjNY96vdRyAmCYl0P7THMnOMjkaKhrAJdVW9p/afd8J8T2mgabplpcXdzBHOs91cmOONWeTfIwCk93HHBIzsD6OU5czVpVRHbHrEPDXENtDrXFfEVglxayyWptLe2lWdmnkJhwykqQrxoC2FKqMnIOYBcvDGqHW+G9J1VrdrZr60iujAxyYt6BtpOBzGcdPCndc02HWdFv9MumkSC9t5LeRoyAwV1KkgkEZwfI0zwsbpuGNIOod99tNnCZ++ZWk7zYN24r6JbOcleWenKunQlNp5RHNW4RtdS1Nbt76/gidYlurSF0EV2I23IJMqWGCeexl3Dk2RyrOk8J22m6v8AbUvr+eKMym2s5nQw2plbdIUwoY5PTezbQSF2g4qRUUI8Dyx2taPp83HurNPZW8jtLu3tGN2SOuetTr+jzBDFw9rqRoAItVKrnmQPs1uep+NRntdXbx7qA89h/wAoqTf0fX/92cSx+Wph/wA7aEf+WgLUl9m/wNKX1RWH9RvhSDKkaLubmRyA5k/hQCm9qn40rp1rXZ5HddibBzwX/lSxArc5WMh/vdPy6UAhJh6QjVpDuPq9Pz6USLK4G9gi5HorzPXzp2LkGA+8azL6n4j60BiOJIzlV9I9WPMn8aTF7ef4j6CnqZj5XE+enon+FALm9m1LrWlnVkYRgv716D8aVslk9o+wfdT+dAZaVI5H3tzOMAcyfwpEjyunopsXlzbr+VLhjWORwgxyFLm9maAQIFJzITI397oPw6VGde4107RdVfTVt7zUNQCiaS3s0UmJD0LM7Kozjkudx8BUsqge1ThCS97QbmfSdVsmv9RERawN9HDPuWMICEZhuXCg+eSeVa6spxjmCyzu4fb0Lit7OvU5Fjd9yF69xZPrnEOsXtzaC+RrqRLRrgsj2sKnCCNesTYAJIwc9a9D9ldzql32faLPrpdr9ojueQ5Z0DMI2J8SUCnPjnNcLs94HteHdCjg1OC11HUpL1rt3aMSCJmVVwrsPJFJ95Nc3jbtAa6XX9F0mBH7iOWzmuDdrCwlKEERAg72UnnkoMjANaKalDM5vfod/EK1G4irezpaw/cv3Y0zjpkmllxtw9PdRWsOpI7yP3UUgjfupXz6iS42O3uVia1OLOLzo+pW+n2dqk2oTRGbbNMIo4owcbnbDEZOQMKxODyFVZoGkahxZw/aQ6Ub1LOeNRHK0e2OHDYyG6EoQeQJOVNWBxLpGl8X609xoeqaXdanawi3uIRcB8KGJUNtJKEFn6qc591c0LyvWoynTptSWyeme54qN7d1qNSUKLU4vGHpnudrhLiG34ihuw0Lw6jZOqXELyCQLu5qyMORQ88HAPI5AqVVFeDuFk4cgvJXdHvLvuxKYwQqqmdqjPXBZznA69OVSh3VF3OwUeZNd1CVSVNOqsS6osbaVWVKMqyxLqjEXqH5j9TXMH/Wo/8Agh/xmt2OR2UiJOWT6Tch1/Oub3bnijDStu+x5yoA/f6VuN526RD7JPhSNkw9WYH5kz9MUiIziNfQjYY+8QfpQD0nrR/N+hpdazyuGTfC49LwwfA++l/aYx6xZfmUigFp60nzfoKJvZP8ppEMiOz7HVst4H3Clzeyf5TQHP4kvJdN4c1S+toBcXFrayzxwkZ7xlQsF5eZGK8wt2g6xaW8eo29xqMusIRJK00u63n5jdGYRhVUjkCgVvfV1dvHFGpcKcDx3ejmSOa4vI7aSeJQzwxkMzMuQRn0doJHLd54qjezWXSeK+0TR9JXSLpdLlSXv4pJmYKUjLK27qMlcHn1IxjpXS+EXtxbu7of4Rzn4Fpw28saHNC8g5N7Y6HqTQLpNY0HTdThE8CXttHcrGz7igdQ2DnyzXm7tQ4Pg4X7S59WFgmo2epB7tEulBQTs57wEdGxkNgjHpjyq/ONeLbLg+1sIfs/fXd2xhtLVHWJcKMlmY8lRRjJAJ5jANQXXO1nSRpF3ZatpFpNqhkjWG0kmWe1nDk/tBIVztUKS2UBzgeORxyrzhCUIT5eZYflv9hw6m4141nR549vPTcx/R/uNSfS9dhFqsGixzI1pCGOyJ2DGVE64XOxtvQFz51b/eyD1oH/AMJBqq+Be0ZL3XrXh2caZLHcxP8AZZtOiaFI2RdxjaNi2BtDEMG54xtFW1WNF5gtc+Jp4lFq4k3T5M6pdkcpLLTIdUN+mn28N64Ie4FuFkbp1fGT+dRrtlukHZlrvdQx3bmNEEZ57SZFG/Hmmd/+HnU3b2qfA/pSbiCG5heK4ijlidSrpIoZWB6gg9RWyeZppnLRmqVSM+zTPHtpqenaJqmjajp1i8c9pOhkfUJGlic+ErKCCChwwCFRyxV69m3aanFuqanotw1pNdwWpu4rqzDLHNHkKwKMWKMpZeW5s5zyrZ4o7IOGde06a3ggfTpzL3izQuzAHHQoxxt59BjoOdZ7POyzTOA4727trmW61GeExPOUCAJ12qvPAJAzzPQdK6rOjaUrKbqybrZ0SWmNOvzO/jF/C9rxlRi1FL9zy92yBf0i4+JbDijRdc0uIy6bb2RijcpvW3nLne390ldgB9xx0rtf0bbPXo7LXL/WoDbWV/cxy20Wzu1L7G72RV8m/Z8xyJB8qs/ibWoOGOHbzWNTuNtnaR73/Z5ZugCjmOZJAHvNQfRe1mG81vS7HUtPhtBqEoht5Ir1ZikhB2xyrtGxm6DaXGeWasFdzrWP6eFFaby69yo5cSzktSkL7V/gP1pHfMPWhkHwwf1pC3EYkcsSvIespFUxsNmkQ+p+J+tCSxv6jq3wOaIfZj8frQBN7JvhWXRH9dVb4jNYm9k1LoDUmt4hLAFQLlj6vL90+VO9xj1ZZV/xZ+uaJvbQfMfoaeoDWCTCU7ZVPoj1k+PkRS8zjqkbfBiP0pY9s3yj9aXQGtHK43boX9Y8xg/rSzcxj1t6/MhFLi6N8xpTeqfhQDME0TRoFkQnA5BhTk3szWFRGiXeqtyHUZpqW2iCHagXmPV5ePuoDZqG9qhxw3H77hR/lapZ3GPVllX/ABZ+uahfaqJF4egDSbh9pU+rg+q386Ak3ZeMcE2B8zIf85qVVGOzIY4H0z4Sf/kapPQBUVsezzhKw1sataaDZxXwberqp2ow5hlTO1TnxABqVUVnCpOCai2s7kYyBAIIIBB5EGoxbcCcO291FKljI0cLiWG0luppLWBwcho7dnMSEHoVUY8MVJ6Kw65J8CMR8B8Ox6gt4lnMJkuWvIwbycpDKxYu0ab9qbt7bgoAbPMGujY8O6VY/wBX/ZbXu/6vs2sLb9o57uA7MpzPP2aczk8uvM11qKbLHrsM65OBHwfoUenXFglji0uLCPTJU76T0raMMETO7IwHbmOfPmelOatwro+rNdNfWjO9ykEcjpNJGwELs8RVlYFGVmJDLg+/kK7dFS23uTl+vXgjk6Bw7pmgNdNpcEkb3bK87STyStK6rtDsXYksQBlupwMk0V1qKggKoTjntEtbjjG/0nTOGNKXWhLDo8l5xDtTvYnuBGO6i9eWINIXJBAxk1fdQ7ieDSeNdIuLKxj0fWZLW/itruKcJL3CrOguFPijiMSY6HOMUBIeHLBtL4e0vT37jdaWsUB7hCkeUQL6CkkheXIZOBXQrn8ODTxw9pY0RlbSvssX2RlYsDDsGwgnmRtxzPOuhQFXdsaWK3lhNqX9TTg2s8VvBqjuhSUlCJbbCMHuBjCxja5z6LDnXN0U26a/Zrf9x/0/OoW4k3c7n7J3Kd5z9buNu/8Aub/79XHRSHuvPrfP9+GhElzL12x68dTzH23Xktv2jaiv9X3UsWyIiWLYwP7NfDdu/hUh/o9XXew8RmOGX0riJtrrsI/Z45g8x6taHbSu3ju6P3o4z/kFdLsBP+ncTJ/4VvzEg/ShJbbRyuD3km0fdT+f/pSoI0RAVUAkZJ86cPQ0mL2SfKKAH9eP4n6UukScmjPv/Q0gzqTiMGQ/3en59KAXH1f5qRcSKiYZgCSMDxPOkIkjl9z7BnmF6/nSmiSONii8+WSeZP40Ab5ZPZpsH3n/AJU3HArXMvekyEBTz6ePhW3TKf2qX5V/WgK27U+0uPhPWrLQ7drSC6uLc3Ut1eKzRwx7iqgIpBdmKty3LjGeddHsn7QI+OINUhdIBe6bIiyyWzEwzI4JR1zzXO1gVOcY6mm+1Lsw0vjtoLu4me01G2jMazqgcMmc7WXIzgk4wR1PWt3s44H0ngDTri1055Li7uWV7iYqNz4BCgAdFGTjOep51aTVh+iTi37btjTffPkYe9zeBSFx28ajO9zqNvfG1m3s1vpps1eAxgnasreuXI6srKAfCvR+i6rHrHDWm6qqGFL61iuVjc81DqGA+IzUGv8Asb4U1LXpNRls5oN7GSS2jl/ZuxJJOMZXn4A4qaaXqOh3ffWukahp91NaLskit50kaEDlghT6PljlTiFSxnCH6OLT/dn7CCkv8jp967+yjOPvPyH5da8W6nbca2tzqHDV/YG4vLud3nU25eS5lLE96D1Y55hh4YxXtmoDxR2hQ6PxDcaPYWkN3ewIklw1xdC3ii3DKpu2sS5GDjbjBGSKw4dxKNg5SnTU89+hmqE675YZz4El0CC+tuGdEg1Z+81KK3gS6fOd0oQBznxy2a839pOnaV/X2s6voaXl9ppuZJLqaOIbY5S37TYSwMg3EncBtGepqzOI+OpeINH0d9DF5a28088d/wB2wWaF4gv7HeMhd2/duU5wORHOqr0XgLWNRvTpOmd73YjYh5JCI1jzj0vec9ADnn7683d3dKpU9hjMt8fgtuAcRoW19O3ncKjUS2a37rzJBqfF8Ok9lj8G2sP2a+uIQlrcWtyLiGffMrTIWwGRmDvy2lcH1jWgjX+jazwnqEmp2MkFjeQpItnasj20TMFeNMZLqykqQAOfhzrscPdi2pRalbpfLCkFvgLcJKGXlgFhkZLAbsAqBnHOpZxFwFf2iQTWlx9uSKTvCkNuEkXbzVvWO7Bx6oBzjArmr1LtPmhT92O/fTsupT8c4hc21w3w736W8m1q298JrL0+ucFgaRr9lr8U50ydSYCFmikRkmiJ6b42AZM4OMjnUJ7SdRv4OJLXT42vU09bUXEj28pieeQuRt7xcMoUKCQhBO8ZrX4bt5uHbu74l16W6gtPsos1SWJu8ndpFKgRj0sjaQMj9/yBqNdoPGVze3kianbXmnBWA0y1FvEzzZ2gl5dxxluqo6EAcycV0VLida2zH3JPuvHqvEqpV615bJUswqSeia137eJYHZVquo3h1ayvmuZra1aN7aa4O6TDhsxlselt2g5OT6YyalP/AO9Q/wDBH/8AJVUab2iz6YthokGnaNp13cIZHvI52ubdmVV3AINrs/uZuQA9JqzcdqU9vqjLLBZLqSQGNpwZDbiLO7vtoG48+Xd5zn96t1G4jSgqdaacsanWpuyjGhdy/wCzGX0z62LspEPsl+FV/wAH8e3V5fx2HEenvaPcn/QbtIikd1yJIMe5zE2MEBmyfceRnUVxEI1DPt+YbfrXZGamsxOmFSM1mLHpPWj+b9DS6iXFnGEWj39rp9nBHeahKhn2vOIooowcbnfDEZOQAFYnB6Vt8H8UQ8RxXadwbW+s3VLiAyCQDcMqysPWU4OCQDyPIVHtYOXJnUhVoOfJnXsdzuo3aTeit6XiM+ApEtvGInKgryPqsRXC1vi6y0jU3sEtr2/vgoleC0RSY0I5FmdlUZxyXO4+VcO77SrS7cwcPWq3riPdM91MbRISSR3ZyrNv5dNuMEHdUSrQjuyJV6cP8pIlPEUeljRp04gubZNMcBZftzIIjz5ZLcuuMc+tR/RtJ4T4OtxqmmNpFjZzoc30k+EZSRy71mPInHIHHKobxLqs3EGp2PEVqGhs7SFrXZOob7Hchz3m4jKqWUxYOeYqquKLcpxtCNSuryx01rf7WotIthLyHazxZGFLCMAsAchSPGtFPikfaSt22o4z1w+3gabGvK/vv0VCDcsZzjTGM6ESveK7zW5xqGs2zXd5JI8kl0ZWYkMc7FB5Ki4ACjkOfnV68A9lWk6pw1FqurGUyajaxS2phTJtlbD5zzBYjaDy5DODzyKYvH0abX4he2rnSbYj7Q+nxx2808JGFPdkhDIG5EgDI8KsqbtPu7i2u7HT7q44bsbZWs7G1tYEmZFUbQZHYHpjACFceZ6mz4nc8NuoU7ilT5J6p65TwtH6R7C3o8YoRdjRk+Ve9otVr899SR2OncH9nF3NqM+sQ6vr0B7i3sYDGkqvJ6PqFiQcE5YkAAnlnFTbhXtDh1fXotG1C0htL24jaS2a3uhcRS7Rlk3bVIcDJxtxgHBNeZori+1Xhi20xzYwWsbDY8qrGsMm/b3hc+rk9WPgavXsw7LodL1a21+6v7O8EasbX7E5eNtyld+/ln0SwwB49eVVFGo21GlHEepu4nZwjCVa/r81Vr3euey8MeJbp9svyn9KXUW4p4l07h27tLaT7ZcX9yrNFaWpDOVGMsS5CIo82YA+GaqziLtcuJ9fubOyvNQ0mytVVWzaRtcPMRkg7gyhFyByHpEEhsV1zqxgsyZ5+2sa91LlpRbZfMf7/wAxpN1/ZZvkP0qFdk/Fl7xbw1Pd3UUBuLa7e1kdAY1lwFYOFOcZV1yM9c1L7qR/s0waFh6B5ggjpWcZKSyjRVpSozdOaw1ozhdpWm6Vq/AmrWPEF7HYabLEveXMjBViYMrIxyRn0wvLx6eNUX2Tdl+kScbWt2+uwXL6bKl5HaLDLBO4U5SQpKqkJu2nIDA9M86tHt00HU+J+CYrfQWdb60vI7wREbe9ChhtBPLILBuf3fPFVr2LcK8YS9oOn61xC91FZ6esy/6UNjSF0K7ADgkZIbOMej516Ph86lLh9aVOuop5zF4y9Onnscs0nNZR6VpC+1f8KXSF9o/4V503A8Ub+uit8RmmYrePuwQGU/3WI+lbNIh9ktAMywsIztmkHuOD+lL2zjpJG3xXH60ub2Z/D60ugNSVphNDujU8zja3Xl7xTvfketFKv4Z+maJf7TD/AIvpT1Aay3EXetucLyHrDb5+dPq6v6rK3wOawvtH+ArDQRN60aE+ZUUBmL1T8x+tZf1G+FMRW6bcqXXmfVcjxrLxOqNtnfp0YA/pQDyeovwrEvqfiPrTaicKMNE3LxBH86TI8oA3Q59Ieq2fH34oDZqDdrJ/9yW4/wC9z/D/AJ1M+/A9aOVf8OfpmoN2rTJJplqqNk72JH5UBMezldvBWlj+4x/ztUkrhcCLs4Q0of8Acg/xNd2gCiiigCiiigCiiigCiiigCiiigCqzl7MGtGn1bh3UzpXFRvLq5+2RIe5uUluZJlhuI84kUCTbu5MMZB8KsyigONwVpM2g8G6DpFy6ST6fYW9pI8edrNHGqkjPPGRXZoooDgcU8Tw8P92GsL6+cwyXLpad3mKGPG+Ru8dQQNy8lyxzyBpqLi60m1kWUdlfm2Mq2/8AWBRBb98UDiLm2/OCOezbk7c55Vze0The/wCIZbRrJLCdEhlhCXsjoLWV9uy7i2q2ZY9rbfVPpHDrzzheGtYGri2d7F9EOoJqb3Bkf7SXVVIj7vbtx3iht+/p6O396kd9fWv418/kktFpv/rT66fjd1n24pt40LfegQ/wrY7Aj/754nX/ALiyb82uB+laf9IO0uJOMLaS3vpbfNqvoBEZTzPM5GfyIpv+j2l0vEHE8V1co7m1siGii2ZAe58yefPqP4UBeUkiRjLsB8fGmYnlaNRGgAAxuf8AQf8ApTscKRnKr6Xix5k/jWYfZL8KAZeHJTvWMmT0PT8q2AABgDApMnVPmpdAIT1pPm/QUTeyakGVI3fewBJ5DxPLypEjyPG22PYmOr9fyoDYJABJIAHia1Fm3XUhhXvMovPOB1bx/lTwgXOZCZG/vdB+HShf7W/+zX6mgObxHfHSOHtU1W53SpY2styYYjt3BELYz78V5ys+3fULT7NfS3v2iQurXOmLZqkAjJ9JYnHphwP3mZgT4V6guY0lt5Y5UV43QqysMhgRzBHlVeab2NcH2OtR6nFZzOUcSR20ku6JGByDjG48/AkirTh9SxhCf6uLb6Yx9TCalpynU7XrHVdT7O9fs9A3nUZrdQqx+s6bwZFHmSm8Y8c4ryzoXFep2fEvDV3qs1tYWGmXcYM0cJUxQZ2yRjbk7SuQVxXtSSRI5TvPVRgDmT18K8ccQcK8T9mHENytnF31nMO7tb2SLeGiJPoZ6KxOdy+PvB52PAZQqwqWrUeaWzlp0w8Mwq6NSL81btfsItUvbbRbSDUreybZNcNerEJXwCVgGG7wjPVigzyBNR7XuCLXtKmh4v4WuYxFqcaPKl0CmGVdh5jPMbQpAGMqefOqWHZ+2n2+k6hxbMmj2+rTTyLEVEbRxps6BiMFi/ojyGeYr0F2LX8WmynhWx3y6VDbPd2csi4kUd5l1cjk2WlBBAHLNUvF6fDaUo2kJuVTr203w86/DQ2WXGp2N0vZS5Zvb+eppcW8Gy8G9imtWujlrvUg/wBqMgTG1mKo7oOqlYgcHOeWeVVJ2ZcRarJx9w3BoOlLZO90kd00DNm4tz7Qzf8AaELubc2SCOVemuJOLLPTL9dPjtry/v1CzSQWiqTGmeRZnZVBODhc7j5VtcKNoN7aNqmgWlrCLhiJXS2EMhYHBVxgHIPn8a22F7a21GdGVJSk9nnVaY+OCK9V3Fd1ZS95792dqL1PxP1qGcd8eWnC2pWWnpbm81S7QvHAGYYXOMnYruc4OAqMeRzjrXN474tvLDXINH0+4ezj7j7TPdRRLJIdzsqIm4FR6jEkq3IjFU7xnf63qPEUmsSXbsbO2isftccIjYo7SOpcAn0iQ4JAA9EdM1Q1b6nGTpxfvLobOHyoX18rBVFGb7+WSUcbdpVlxZYWNraabdLcafepNdDeuAxV4wkf77Nl84KqRjmB0rkXmiNxBqdvp2oRT6RHBBLfyXF6yuFjROeNrEHmRkAggAkjlioToqtPxta3V/dxqsz/ALS4un7qNWCHDM+Dgn1fDmVyam2pLp17ZXD/ANapayQLIsbO5aO5yNssaSgGN8xtINquWJwMVU1k61eNV03JY3T007o5+PcOrcJ4tSnTouTglLny8ZWXnGem6016pnF4T0zTory21O8u7aOCM7SYZkmktSx2iSaPcPQwWzhtwz05VZvGXCOg6eY7XUL1lvpoe9hkWEu80iOuIwiKzlOWSACRnOfCoLxah1DSLeGE27tAyxQiCIAwox2sOnJcZyDXXlNy+tpeyXGqSTSQi37yWRp3LFiTtGTtDZHooABt6VojeWmHJwzLZd/H/R56/wD+RUuJ1ZXd5HnqtKK0w8dkvjldTq8O2Wm32q6ZcXurWNrBFepInfXyCSWSNgwRUJ3Bs7QQwVgG6VeMPslrzlYtvvdTnS4ilS92W0yzRhu8ZRkqff6YBXqMDNWd2c8S6LYcEWVvfcR6TJNaRMXAvIy0UW892rDOQQpRcY68qsOE1aUVKlCLXV5N3A61GKlRpwlHGr5s/c3eNuDV1q/i1CzMC3giEDrNkK6gll5jO0jc3gc591NaVpWn8B6Ve6nqtyVmuDEjm3VjnGQkaqMljudueB16ADNed7niHVLlLm71K3J1t3aRtQMrJPbvkkLG2cxqvTYMDHhXobUNKueNez7h+eaaE6kqW98xRwI2m7oq4yueXptjHiBW9QoyqTuaUc1Ej0nFP+Ovhklf8idSSeMPfReOCuNdvk1HiTWdQsdK1lwTG12GMW6JljVQPRchhtAOFJYHdkCoJ2i20/D2raRqMdpBqukalam7QPuaCSYsQdwIG4qgjJVhyLGrQ07gPWoDIi6fMivOz5N1HlSx3Fmw3TJPTJwKsnQeF7TTeDrfRb6CC8ijDu6SoJE3szOcAjoCxA5dKz4FKFK/d1c27a7N6PPbseX4fbSrXM69Sk4Pu3pnwRWP9GK91CbT+JC+ntbaS13HLbInNVlKYlVSTnACxYHhmmO2rUbDibW4tM0V4Rq+kg/abi5cRwqHwe5JwSz8geQwuTk5zi9bW3htbeOC2ijhhQYSONQqqPIAchXnri/si1s8Z6ndaXDDfWep3Ul2HMwRoS7bmDBvAFuW3PLFXF7UVec6tCCXaLxjHx0Z7XhHsqdePtqjppJ+8s6P4alX2nC02sFr+W5QSwM6PCQSY3U+ry9HngHOfEVZnZ/2c23EEkE665pr2exJpra2m7y4UMAdjr/qz4HmcHzqVT9k/wDVXAV1b2d1PLqkgEtxHF7KTLLvVRtLH9mCo5jJAOBnFc/Q7C/1DiDREse7STTrlMtDFsNvDn9ohIHogoGGDjJIqju72tVrwhdwTWEo8scJLPXCx1Kup/yK/wCG3tW3hUlKnVl7rSed8Zb3Tx26FRWsmq6ZriXNxEkOoWiNBibL9w+87guc7cDCgZ8CepNW52Fa2+natqVprTm2TWZkksVERWGSYKxlwQMBmGw88biDjnyqxO0Hgqz4o0C+twsKX8qKIrl41LqVYMAXwWCkrg48CarHhPso4gTiawutXfubWwuo7rc1wH71o23LtAz1IGc45E1tVOpSqprLX0PaSvbK/sZxko05Lzcn10fiyS9sPZ/qXEWt2usaI5e4S1FrJAJRGSquWBUnAPNznJHQVxdC7J9M0vSbrUuOtTFjNK8Y7w3SIsSgHCs7gqSST59Bg9ausvMJRuiB9E+o3w88VSvbkmu2/FWl6zaRN/V9taGOJ5I96wTFzvbPRSV2AHPga21qVOLdWSz67HDw2/vK8YWFKagtcPRPq8cxbXCVhpWnaHBBoHcnTiS8bxSd4JMnm27J3Z866d5/ZJvkP0qp+wGDU7eDXrvU9lvZ3s0ctvFt7tTJtPeSKvk37PmOpB8qte7INpMQQRsPT4VvpSUoJpYKi+pSo3E6c5czT1ec5+I/TUqI7pvVW69Rnwp2kN7RPxrYcoj7NEPVUr8pK/SkLCwd9s0g6dcH6itmkJ7ST4j6UAjbOOkiN8Vx+tIieYRrmJWGP3X/AJitmkQ+yT4UAzLMdnpRSrzHhnx92aWLmHxcL83o/Wly+p+I+tKoBlmVrmHawIw3Q/Cn61ZYYmuogY15qx6fCnPs6j1WkX4OaAWvtH/Cl1rLHIHfbMfD1lB8Pdil/wCkD/sn/Nf50AuH1PxP1ol9k/wNMxSSBBuhYjnzUg0S3C904ZZFOD1Q/WgNgdBSZei/MKSk8TclkQnyzSpP3PmFALqvu11sWdgPMv8A+WrBquu2BsRaWPMy/wDkoCw+Dl28LaUP/t0P8K7FcvhUY4Y0j/wkR/yCupQBRRRQBRRRQBRRRQBRRRQBRRRQBRRRQBRRRQBRUe46NxDoE11a6rqGnSW/pKLJYC87H0Vj/bRyAZYgcgDk1FZ7ziPTLe6kvNfmuJtCtLaS4jW3gC6hI+TJv9DIGAFQJsweZ3ZxRah6ET7fRjiewPnaA/52rn9hLbeMtaX79hCfykf/APurb/pDX1nb8UaZFcXUEUzWmVR5ApI3tzANczsQmjXje+beux9NJ3Z5HEq//wB1AXzSIfZim+9Z/Yxkj7zch/Okxw71zKxYc/RHJevl/OgMyzISFT02DDkv8+lZ2zSeuwjXyTmfzpbgKihQAAw5D405QDMMao77Rz5czzP50ub2T/KaF9o/4UTECJ8+RoBdMj+1t/sx9TWBMXGIUL/3jyX8/wCVNd0XusTNuynReQ6/xoCg/wCkhr2q6fxVpEH2UXuhfZC4t5Ce5kuN5Dd4vR9qhCAwIG7Ndv8Ao16lrOrabrwvElt9Ginj+xR7iyxsVPeRozcwowhCjkN3Kriv9Ps76za2vbS3uLY8zFNGrp+RGKcs4Iba1ihtoo4YUUBY41Cqo8gB0q0nfUJWSt1SXP8A+2fHOxhyvmzk5Wua9o/DTQnU7oQvcZWGJUaWaZh12IoLvjlnAOKrGLt5sDfwjUdDu7HRrmY28d686O6P0PexLnu8dSpbdjntNaH9IHhPiq+4msNe4X+0zRx2X2SSO2G6SM72YkL1IbcByH7vOqh0HhA6txQ5441lbGyW4T7a8u4guvLu3dQUjkPq/tCpGTyJ5HrteF287ZXFSquunVb9PExlN5wkTjtxbivRO0y91a2h32N1bwwWk7xb1SMKN8QPQZfeSvjkedWL/R00K+0Xg65udbtfslzdXLyQxuCndwHBChT6o37yB4gj3VMbrjfQ4L57STUIoWjfupZnRzFE/Ta8gGxG9zMD7qkKQr3pL/tGGCC1cNfiMLi1hbeyinH9y3eMohQi5c2c4+hW3F/CN3c8Q3uq6bFJcx3piMgWURlXCiMY3YBXCrzz1J5VVvDHanDoFhfz2Mumz2kl09ybC4ZxNOMKpYSA4QkICFKNnqSM4Hp269kPnT/iFU3qH9Hvh+51x7qC+uLbT5HLtaJGpK5Odqv4Dyyp+NcvCLHhkLipXvHJNrTGq8dPE5I8Op0a8rmnnmlvrp8iwjp2lcZaJp2poZ4454VntpoyEcRyAMAQcg8sciDjniqUgFzNolw066hHd3ALsjy5iTHRHhI2PjAyWUnIyMYFeiNNtbfT9PhtLSNYbW3URRIOiIvIAe4ACuTccPaNd6j9qGnQyytuLZyI3J6ll9VjzPMg9ap72ylVmqlu1GXVtatGu9sKtSca1rJQn1eNceZ5ts+COMGtooBp96TeWwyxiG1kYA4Z+i+GQSCDW1Z8B8aXyxcPul7HFGEjaRgO5iCkYYOPROOvIk16gliZo2aVyxAyFHJR/OtgAKAAAAPAVsVlFfuZ7j/5LXcOWVODeMZx9d9yIWvAmki4MkwmkgB9G0aTdGMY8SNzDl0JIqKcacMPY8SRTaJFciBrXcYYA0hiYOQzKMkjIdRhRywfM1u9oHahBwzrUeh2MMUupSHdJPcMRBbDGcsB6TNgqdoxncPSpvs745fifjSawujZzTW9g8sdzaKyJKhkjByjFijAkctzZzmtdW0tqkXRjiLfbR5PJ1OAwr2sp04csM/5RWMPON/PQrO7s57jXBJcmeXT7jHfwTytHHPIg9EOgYBvHkwz+zHnWtqCSNxFBZaXYsYYCL2WysgojicZVWUMyohbJO0cyVXka9G3HC+i3F8bubT4WmYksOexyc5LJnaxOTzINVL2gdlepXPEE+p8MRp9mvBH3ltDIsPdsqhOQOBtwAeuck8q4Fw64prEpuUdsLf5nJwf/j3tq/sb255aeHj7ZfT8kRvdT76fS9YsJGmuEuTAJLhQnduQV2yZ9IYJz0PMcuuan3Zhqk2j8Uz6XJcWt5DrB76I20ZgSO4RCZAU9L1lGd2eezpzpvhPshns7dk1u6h/a3P2kmBi7l8DGSQAMFVJ9bPP405rrWvBOrQW1vNDfcSy20slq8qrBb2akbBNJncxOdwAXOfSGB1pa29zQqJ493O7euDRS4beUL10bbM6cZNKTeW4rql4kn7Q+KL7RZbCxsR9mmvmkZ7nuxKYo0Vc7VzjeS64yCOvI1qcC8XXl7rN3pGo3D3cX2U3NvdSxLHIMMFZH2gKfXXBCr0Oc1UcEkmqwTwW9on/AEktZUVrrv8AvJ55WxtJkzmRH6AHl7hXonReHrLQ4Jza97JNIm15pmBZgMkDkAB18AP4V1Ua9e4uW4PEI7p75wZ06l3VvZR/xhDSSaec4+T75OxHIjj0HVvgc1Ce2PVLvR+BdRudMuPs96YxFFIGww3yIrFT94KWII5jGfCop/SG4oNlw02maFM0upLcRNqEVqG7yG12ljvdB+y3HYMkgkMfDNU9wCdU4x4z02y0nTIbG0jV7ieKB2SA7UIWQqBgNkhd2MncMnxr0ceHVq1nVuqLT5E9MrPp9C1nWlb4moczWqXfHT4nN4ivpe6trzTLFNP1O3bMd5ayss7k9Szggs2ee4kn8DivYPCct/Pwzpc2sJ3epyW0b3SYxtlKAuMeHpZqobjSbfgWS24o1yy+ztbz91bW6NG8tzcSKVVeu0DBdslgRtzipXwf2lJrHEMWh3tta299cxvNbNb3XfxS7ebJu2ghwMnG3GAcE1X2Ea9W05p02sNvL7af2dNxxOHEWq0KHsdMcreX5ljTezNLrWlkkEZ3Qt8VINL+0Rj1t6fMpH8azNJz+Jdas+HdIu9W1JmW0tYi77RlmOQAoHmSQB7zUO0XtPhutYsLLU9Pjsk1CQQ28sV2s5SQ+qkq4Gxj0G0uM8sipRxdo1nxXoN5o9xMFiuYwN6nJRlZWU4zzwyg48cVW3CXYw+m8R2moapeW0kFlOtxEkG7dIyHKlsgbcMAcelnGK0VJVFJKCyi0s6NlOhUlcVHGa2WN9PyXJGAVYEAjcetMXcEQt5WEag7TzAxWxF0b5j9aRef2WX5a3lWHcAepJKv+LP1zSGSYSJiUHr6y/yxWzSG9qn40AjdOOqRt8GI/SkJMwd90Mg5+GD4e6tmkJ68nx/QUAj7TEPWbZ84K/Ws27q0SbWU8h0NOHpTKQxPEm+NCcDqKAcl9UfMPqKXWtJboANpdfSHRz5+VL7qQerO3+IA0AP/AGuL5G+q09Woe/F0ns3OxvNfEfGne9kHrQMflYH+VALT15PiPpS61kuEDPvDrz8UPkKdSeJ/VkQnyzQGYfZrRN7J/hRD7JfhRN7JqAyyK49JQ3xGaYkt4gU2oFy37vo/StmkSetH836GgEdwR6k0q/jn61XPa4HB00O+/G/HLHXH8qsyq07XTmewHkpP8TQFocNDbw5pQ8rSIf5BXRrT0RdmjWC+VvGP8orcoAooooAooooAooooAooooAooooAooooAooooDWv7G3v4o47uPvEjlSdRuIw6MGU8uuCAcdK52qcL6Rqmqwaje2zvdRbOazyIkmxtyd4isFk2sSy7wdpORit/VtUsNHsXvdXvrWws0IDz3UyxRqScDLMQBkkCtd+INGjuNPt31bT1n1Bd9nGblA1yuM5jGcuMEdM0Xh6YZUn9ISBJNR0syIrq0LKQwyPW/wCdRbsMtLa17QZkt7eGEPpkzkRoFyRLCM8vHnUy/pBL+10hvc4+lRDsYbHaWq+ekXR/Ka2/nQF/UiL1D8x+ppda6zKhZRln3H0VGT1/hQDsvqj5h9aJJEjxvYDPQeJpmQSuuWxGuRyHM9fOnY4kjOVX0j1Y8yfxoBoNK8jd2oQEDm/X8qy0C7WaQmRwOreHwHQU6PbN8B+tZf1G+FAZX1R8KaP9rH+zP1FOJ6i/CtZ5h9rXugZG2EYXw5jxoDab1TTImRERc7nwPRXmaDHJIP2r7R91P5/+lLt1VYl2qBkAnA60BV2vdq8Vtrmo2Wm2MdwmnSGC5kkvFhZ5BzZIlKncw6HcVGeQNefdF4W441fS4YdFW/vNIvlcxyhR3Uisx3F29UNkHIJyCPdT/H2laPrPEmt8Q6JODo8t3JK/eSL3znce9liTPpJu3EZKnHhyr1X2e6Pp+g8CaRp+jXBurBLfvIp8Y70SZkLgeAJYkDwzXqlWo8IoxqUPfnNaqUXphfzlmjDqPDKqsODNe0zSodCeG8nKwmImNcwzcubb+g3dfSIPOpPd8VXugXEPDllcWQm0u0t4bq+vY3l72XuwdqorKeYKsWLHG7GDVnmRI41LsBkcvfUQ4h4Pi1rVJL62lFnPIFEpeIOJMDAbGQc4AGc9FHKvAztKtup1LZ80pPZvT4FXKwrWcJzs25Sk9pPTHZHlviDibWo9T1AX8K3WtmZnGqRyuJomJyndN1RAMYRcDFevuGbrUrrhvSZdTg7vUpLSJrreu0LKUBcY+bNcIaVwjwtJapeS6VDqssgaGa8aJLiRiw9TOD5Dl4CptXoa94q9vShKmozivea6v7FnbRqKC9q/exr5mvFCrZMp3kMevT8qdb2qfA/pRF0b5jSZXVHVnIUYPM1xHQKm9k/wNKZgoJYgAdSa15JHkjbu0ITByzcs/AUtYF3BpCZH826D4CgKy497NV4n1WXUdPeFLiVgztNkDIULkHByCqpywPVzmq94o4SteANTFzqPdahaGx3ESIFSWTvDlNmTuAxFybIJIPhy9JR/v/Mai3G3D9txQW0i8YpHcWUuHAyUdZYWVseOGAOOWelcNayjJN09JPXPruZ89aVB2Ua0oUpSTaXmm8efyzrgr3s14un0nUodL1Rorew1OZEsI4rj7QLSUg/snBwUDYXaq7lByOWasTjHi224P0iG71BRPJPKILe3iOJJpD4DPIAcySSAAPPANLjgccI8ZaYt29pfXULrfRQpMYUCo3oPK5UlBuHIKr52kcutS3izS17U9Mh+yx/ZtZ0OVlktXlDKRIAdyMOTA7MAnb+9kDAqKdaUYOOPeXTOWdd1HhlvcwoW9VyhpzPDytddHq8LX+CS8N9osOq69b6Rf2Udrezq0lu1tdC5ik2jLJu2qQ4HPG3GAcE1odqfZ9FxffW+p2lzHb6hFD9nZblWVJEDFl5gHaQWbwOc+GKi/BPBdvwRrdjrvFdxFa3S71srKDdPNI5UqzbUBLYVuihvWySMc7al1pNW4W1G+4WnjvLpIJRAAOYnCEqjKcFWztyrYPOtsf8AuptVV8DdWuaXD7tVOHVM8q3x89GUJa8Gpw3rl/b6haWGoSFIzGZDujKbcllU+IYuu7AIxkYzVw9lkmoPwncrqLySRR3MqWjySGRjDgcixJJwxdRnwUVUU1lJcWdvLbWdvdavvR47qV+8muZcjCyMT6YY4G0kgVMO0DtQh0Hiy64e0+axsGsokM9xeiSRWd13LGkasvLaVJbPLONprk4LRqXtebtpOSX7cbfnB5G0v6nE7yrfTquSb2axhv8AGClIJtb0e61O01C+ni1AXUz3hxnvZAxDvn94defTFTjgnjqXgzgyJDb2FgLRJZB9rtpO81LdIWGxhtXkCEDftPDkBUW7Q+OYOI9Ohu9MtJrS4ecR6u9vJvVmzgGM4AIKxg5I/fHvJ5cWq2vGWtWGgz38+laRdZ76XVLvvY4XRdyuru2QTt27dwGWGBV/R4LdVHUulHlhGWJa5xqm8LHZ6LXzLu841c3tGFvyxSg0sxWr8/h9SV9rPF83F9paRa5AbawkMbWlrY3KXJguMNkzDarFirMoCkj4nrIP6OnZ3ajUE4ve5Mi2zPFZqqkK5aMAyZPhh2XGOoPlUS1DsE4lt7iA6Z9mvIGIdLmGcKFHUMQcH3+jmvRPZpoacH8EaZoctx3klqr75CpALs7O2MgcgWIHuFXd9Vp2Nt7CwueaE944+uqyui317HHCnJ1OeRKpvZml0y8iPGdjq3Toc+NPV5o6xl40eUb0VvRPUZo+zRj1QyfKxH0pf+uHy0ugNaOJwDsmcekeRAPjSboTi3fLRsMeRBrYi9U/MfrSLv8Asz/CgDvJR60BPyMD9cUhp1EiblkXkeqmtmkN7VPgf0oBKzxMcLIhPlmlR+tJ836CssiuMMoYe8ZphLeLc+F2+l+6SvgPKgNg9DSYvZJ8BTbQsFOyaQcuhIP1FYjWcIuHjYYHIqR/HNAOy9F+YUutaR5ht3RA+kPVbP1xS+/A9eOVf8OfpmgA/wBrX/Zn6inq1BPEbsftFHoEczjxraBBGRzFAJj9aT5v0FZdFf11VviM1iPq/wA1KPSgNeK3i7pCF2nA9UlfpRLCRGdssg9xIP1p6H2SfKKJvU/EfWgEbZx0kjb4rj9aQ7zBk3RKef7re4+eK2aQ/tI/ifpQCO/x68Uq/wCHP0zVadqsiy6hZBTkBB4Y8Wq0aqztXb/33Zj/ALlT/magLi09dthbL5RKP4Cn6RANsMa+SgfwpdAFFFFAFFFFAFFFFAFFFFAFFFFAFFFFAFFFFAQztIt7hm0S7jk1CG2tbl3muNOshd3EBMbKrpGUkzzO0kIxAc8hzZYjFBqUenXVld6RejU9WtbSKzmgsCETZI+GlKDZAy5EpVtoyxC5OQLhootA9Sl/6R7XUcGhvaQQzZaUMJJSh5BenonPX3VAexm7uW7TLXvbKSBzp9zGN0ilWy0R5EEnlt8QKsv+kGM2WjHykl+i1XXZa23tM0f+9DcL/kB/SgPQfdPJ7Zzj7qch/M0uBQqsqgABjyFOUiP9/wCagCb2Z/D60umrh1WI7iBnpnxpO+WT2abF+8/8qAWSFlYsQBtHM/E0hpi4IhQsPvHkv/OsLCvfZkJkbGct4fhT56GgGEh7xFMzFxj1ei/86yQFuogAAO7bkPitOReyT4CkP/aovlb9KArjtM1jUouIrXTYmvIdMFqLiQ2sphaeQuwCmRcMoULn0SCd4zW92VarqN5/W1lfNczWto0TW01wdz7XDZjLY9LbtBycn0xk1K9Z07TtVRYr+2FyyZ27SQ6ZxnDAgrnA8R0pWlabDY2iwWkaW0HUrEPSY4AyzHmTgDn15da4o0a6uHUc/c7FdG3uVduq6n/X2xrt6Z5e437GV0XiX7LY3IOnTqZYGk5Mo3EGPGfSKjbz5ZyKuTsagv7Ww1KwEjjR7XuUtQ8hlKNsIdFJPIACM46DccVYdzY2lwncXNtDNCwO5JUDhunUHrWxFFHBAsUEaRxIuFRFACjyAFWN5eX19VhK4q5hBYUcJfNrcyjaVVc+19p7n/rj7iYIkRQwHpEc2PM0se2b5R+tZi9mnwFNySLHKdx5lRgDmT18K1neeSe0f/pdo3H3EsU1os0erXbmN5YO8+0QHlHGD+8FTA2joQfGpfoHaZqfB+iaXwpqctlZ6pptohup9SR5SN5LxQrGrKRtiaPLFuXTacV6BumleBiFEacuvNjz/hVc9onY1pPGOsf1qLyWyv3VVnfYJVlCjAJGQQ2MDOcYA5V6GlxGzulToXdPkjFayjq28YWTS4SjlxZ3ezHjL/pzw2+oQQx20sNy9rcBX7xBIuDlDgZUqykE+eOeKqr+kdq2q6VxVo8b2hvtEazZ1hnJMMtxvIbevR9q7MKRgbs1c/AXCmncGaAulaUHMQkaSSR8bpHOMsccugA+AFVdxZfXeu6vq8GspetbwXUkNrbxybIolQ7Q5TGJC2N3phhg4AxVNU4nZcMufb1I81LLST0ytcHPe3tO0pKVaWM6ET7Je1K90uLVNLurPvI53Wawgmu+7gtEwRKC7BmVM7Nqqp5lgMVenAHG1nxhb3ywxG2v7CRYrq3MgkC7hlWVxyZGAODgHkcgVUfFvAKcd8McPatJPb2GvRWzWf2Xuiq3EaSuEZUQejn0m5Lj0/ACpb2Pdnd3wXp18sl2Laa/ZDO6rl9qA7VGeS+u3PmefQYqyu5cOubf9VQlyzl+zD0Xn5fU30ZuaTWzWclm3WoW1jkXEmJHbCRqCzufIKOZrQI1S5v4r6C0hhRI2iWO5lIdgxU5O0EL6o5c/Gt6z0+ys9zwj9q/rylyzv8AFjzNcbtC4gn4W4O1LWbePvpLdFEaSdC7uqKTjngFgTz6A1SN4WWdMIOclCO70Ky7cdVXStY0We9tLe0v79Xtu+nlMkAijO4ucYOVMnJcDdu6jHNPYpxlpCcRa1ps0tvLcSwR3Ed9bKwikiQldjISxjZWkJ9YghvDAzXXF2qntAvIINX4gEcdipf7RcWiDErgZjiRQCEwFJLMx5D8bH/oy8P6fa6VqesRQl9WW4fTpZg2Ywi7H/ZjrhtyE5+6MY8d1CnwmVKVZJ/qO/T+e3gY3HAJ2ld3dSnh7N6+X2JDx9ZSahxFb6vpN4bqP7ILUpaMJHjIdmJ2gknduA5D9znUF4nvte4NeBmlvbaHXX3zCNgk5SBR0PPYXMwBPJh3fvq/57KwuCTd20MzHqZYgfqKgXaX2ZWnFtpZto9x9g1GyZjE+5jGVYDcpGeWdq8wD06eVfDh0J3PtfaOLffVLxwtTns7OhQ4gr2rzSXWOdNsaeJGexLiJ9S441KzMEjQyWRukluj3s8TK6KV705dlYOD6THG3lWv26cF6LrHFNvLaMY+IbqESTh2Cwd0voh5D6wJxtG0Nnb0HUyDsy7K9Q4T1CfV7zWo5NWlhNuAkReNIywYjngnJVfAYx45rr8W8I6jrWqJfodOmuUhEDevGGQMWX7wBBZvPrXa611wvM7GpzVF1Wied9/ujfxqsqnPUsKWFpiLa+Ovc8o2WuWtrw7PYfY7+O8Z2dSJf2UbZGFaM+i/qjJZSeXLGBWtoOt6rp2o3d5YRQQ3Ew2FZI8mNPFBnw8/OvUuh9nukafcPe65w0b29aTeGiCyRLy8U3+kc5OStda+0Dgi74gXUtQ0m3jvGLPIbmB41ZyQdzKcIxPPmQa9Rb8esv8A7ZW7UpLMk3nMvHbPmcVGlOUFOS5ZPdf7Of8A0drHV7Ds7Ua1GYVnu5Z7OHG0RwMFIAX90Ft5A8mB8asyLo3zH603bXltdDNtcQzf7Nw30qluI+2g2fEWr6fp0mlW0Wm3D22L4Oz3UinDgFSBEoOVDEPnrgVRezq39ec6MNXrhdDsyoLUn/aJxfp/CdvYrcW63N/fyGO1g3LGG2jLMzn1UUYyeZ5jANafAnHFjxRqd5pRi+x6pbRCfZDdd/FLETjfG+ATg4BDKpBI61GuK+HbLtu7P9A1yxkNhdIJHhWXLKCTsljJH96MYbH7vTny2+xnsmHAV7d6nfXcdxqU8P2cLDnu40LBm5nBYkqvgMY8c10fp7ONpKU5tVk8cuPHvtsY5lzaLQs7u5BKNsxPo/vqD9MUvM48In+BK/zpf+u/w0uqo2GtHKyqd0L+sea4PjSbq4jMDAllPL1lI8ffWxF6h+Y/U0i7/s7fh9aAcSRH9R1b4HNYb2qfA/pWHhif1o0J94po26CVdhdeR6MfdQGzSI+r/N+gpHdyj1ZifnUH6YpEZnBf0Y39LzK/zoB9/Ub4UR+ovwpl5XCNuhccuowRWUuIgoDMU5fvKR9aAck/c+YUumi6Ps2Mrel4HNO0AwQGuyGAI7vx+NZNtDnIjVT5ry+lA/tbf7MfU09QGtHD62yWVfS88/XNKKzKDiVWH95P5GnIujfMay/qN8KAZjaZY1zGrDA9Vv5isSzHb6UUq8x4Z8fdmn4/UX4ViX1R8w+tAIFzDnBkVT5Ny+tKLBnQqQRz6UsgEYPMUw9vEZU/ZqDg8wMGgNiqo7VzniO0X/7df+NqtHuAPUklX/Fn65qrO0hSeKbRWYudiLkgefu+NAXfRRRQBRRRQBRRRQBRRRQBRRRQBRRRQBRRRQBRRRQHF4z15OGuHbnVJBbERNGg+1XAt4tzuqAvIQdigtknBwB0rgR8Z6lcWVnJpum6RqU8sEt5K1lq5ltxAjBf2cvc/tHJJwu1Vypyw5Zk3EemS6rpvcW01vDcJLHPE9xarcRh0YMu5CRnmBzVlYHBDA1Fv+hGqRCW4s+IIYNUvO/W+nFhmN1lKk9zH3n7Nl2jaSzjJYsGJ5Rr68tPrv4E6aEf7cZ4r/hrQ762bdBMxkjbzVlUg/lVb9mp29pPD/vadf8A9RIf0qyu3fSbZOCNKs0V0traVY4wkjIVCrgc1IPQVUvZnZ/Zu0nhoC6unR55l2ySbsf6LOeRIz4edZSxl42MY5ws7npqSZIzgnLeCgZP5U0neyF8Hulzz8W6flT0caRjCKB5++hPXk+b9BUEjbQokbsAS2PWY5NP0ib2T/KaUSAMkgDzNAJ/13+Gl1rd8Xl/YLu5YyeQ/wCdK7jfznYv/dHJfy8fxoBMc47tViUyMAAcdB8TSHjd7iLvm5EN6KcvLx8a2YfZJ8KRL/aIf8X0oBxEVF2ooUeQFc/WbybT+Hr+9tYftFxbW0k0cPP9oyqSF5eZGK0ePtSvtJ4R1G80pd16qqkZ27thZ1UvjBztDFufLlzqo5OJNb0doLjTLzUGleRYpxfStcxyBjguEJ9ArndhNo5YIxXFc39G2koVHhsr7ziVC0mqdWWG9huXifWdMs11c32pS6hCBNO01xmCdeRaPuvUQEcgVUN76vKz1Ww1C1W4068t7yB8hXtpBKrfArkV54vIQ2u6fIly1xCpeRUuLZVCyhcghEUJtChjyUEc8k8sTTg231sXfEGs6WEkaXTJFQrHhbm6HsT5MRhwTn94edVthfS9p7KcufPVLTBUcL4jP2vsaknUzs0tEku5bEYlkReYjTA6c2P8qXHGscp2jqvMk5JrzxAL2GC2utIjVtcDIY70TEz3MmR6EjZy6scDaSRXor/Xf4as7O9p3abp9C4sOI0r5SdLOgi7/sz/AAp6ubqmo28Aa2DNLdMPRgiG9z+A6D3nArVLX19n7XMdNgP+ri5yn4uRgf4fzrsO83LrU7azkMUjM9wxJWCJS8jfgPqeVcHUOGl1+8F3f2kVjzBPdtmaTGMbyDt6ADBDfGpBZWljaRFbREQE5JVssx8yepPxpjXbq5sND1G9s42lmtraSaOI8zIyqSFx15kYrCcYyXvrKMKkISjiayvEi3aLdS8C9mus6hw1aQpfQQqkLBdzKWZU3nOc7Q27B5ej5V5bseMtagezn061ZdcSRHGpGV2nuHyMiVicurdNjEjFXDLresQ2X2xptRvr8qDcRzy95b3an1oTBjYqsOQ2qDz686O1rTeHOBrzSZtIs7ewvtTkdA0+Wt4kQZeQD1gfTUBQQDnw55sOCcXtqtGpTo0Pa1HtrjXHrO/5q4cQjd05TtHzOPTb6kvk7Slk0a07izt01ie4ltpRM7PDD3YVmkyACwxJGQvo53Yzy50Vfa1e6nZ3kmsWkVxqkzOZL13JlibJ9FDn0UXpsHokdRVk9nGo6Nxdc3XDjSW51G0R9Qg1O0j9GdWIRw8bZ2kHuhgMchV5jHPlcZdiDQTXupRcQ28emsXubsyo6CPJyxVRu3ZOcDrzxzrgo8Orzrujf1FRSSecN69Vj6oueCcSq2VSUruiqkXFYaeMSW/wOV2c8IWfF93FFHftG89it333cBlDoVSVDzGTuYYbyB616G4O4ds+FNGGm6UheMu0skrEZkc4yx5Y6AD4AVW3BercPcBaZp+nQ6RxCwmUoL2SGMrLgs5OzvCyAksQhG48uRIqCdqnEdxqfaOYryRZuHJrWGSwkeHvEWIoC8iRN6Pelyy7mGV24xyrXb0KMHUkpLEcvP8A+c4WnfVHRQv7/iSVpUqOo220s+bX0JlN2zzTd9qFommNYxuxisZt4nnjB9bvAdqMRzClG+NXFpepWeraXZX9oN0F3Ck8W5dp2uoYZ8uRFeaOzrhbR+J+LJdHguLz+r4rQ3Ku0aiUgMqlC3IZ9MHO3n5CvTtqlrp9nBZ28QhghjWOKFR6qqMAD4ACsLec55csY6Fjxm2tbVxpUVJT/cmsY0WB0RbhksQD4KeVYd+6IVXy3ggXJ/hSFXvjn0Yl8lI3H4+VO92kQJVimevvrpKQQVnkA34VfFVOD+f8qgfFXaTaaDr8uhafZQ3F9bRrLcm4uhbRRbxlV3bWLORzxtxgjJFT8d6ehAHmw51S3av2Ky8WcSy65pl5DDc3CoLiO4ZtpKqFDBgD+6FGMeHXnXdw+nbVa3LdT5Y43xnUxm2l7pPeEdY0HjnRf6xt7GGMrK8E8c0aGWKVfWUsMjxBBB5giodxX2EaBrWuSalaXstgk795PCEEgZj1KkkFSTzOd3M/hUu7L+D7fgThYaVbSvcSSzNcTzMhCtIwA5DnyAVR18M+OKqDtf7Qr7Su0W/0u4/rJNNtIohbpYztbd6zIGaRnXDHG7aFzt9HmDXbw+Fz+snDhcnnXD7oxnjl98uTTdFTg7hlbbT9SFtounQtIftUCuFQZdmJXaT4k1BrXttKw295faZajTJ5FUSLeBZolY4WSSLBAU+5yRnmK6XZBq152gdmWo2/EP2mZZJbjTjM+EeeAoMMxAxuw5XIH7tQew/o3uutJ9v1W3l0lXBbYrCWRc81x0XI5Z3H4VFC1tlOtG/qOM4+DeXrn45DlLTkWhe66rMrhrjS71OWCY1WUf5ST/CnF17Td+yS6ED+VwrRH/MBW+ZGUhSoJ8lNJYlwRKrBTy2gZB+NUpsCznini3QSxyLk80YEdfdWbv2B+I+orQudL0iQbpLO33eaR7X/ADHOmV0YMQYLq+tYh0QXBf8Ag24CgO3SD7ZflP6VzTbapCC0epxSgeFxbj6qV+lIW41hCGksbacAYzDOVJ/Bh+tAdikR/v8AzVzv63MbAXOnahD5kRd6B+KFqxba5pjsy/bYo2JyFlPdn8mxQHTk9m3wNZX1R8Kb7xJYGeN1dSDgqcg04vQUAzNDGxTdGpy3l7jWfs6D1Gdfg5+lLk9aP5v0NLoDUEcgunCzEkIvN1B8T5Yp3NwP3Yn+BK/zoX+1yfIv1anqA1o5WAbdC/rHmMGsvcx7G3EqcfvKR9adi9U/MfrRL7N/gaAxE6Mg2MrcvA5rMvRfmFJMMTgbo0J8yKbkt0G3YXX0h0Y/SgNmkN7VPgf0pHdyj1ZyfnUH6YpBM4lGRG/onoSvl8aA2aqvjsCTjizT+9GPpVnd649eFx7xg1WPFDCbtFswAR+2iGCMH92gLqooooAooooAooooAooooAooooAooooAooooAooooAorS1u/Ol6ReXy21xdtbxNIILeMySSEDkqqASSfcKqnhrVLniG4Gl6pqmtCOfWZhMxW501z/oqyLDGxCOqBtx2qQ2FBbIJ3Fq2uyz9UiG8Yb6/hv7Hb7d1zwjA3ldKP4GqZ4Gfu+0bhR/K8kH52s6/rVjdo+pzT9jel3k4nvSbsKsseHaWMGRUlPPnuUK2R96qm4K1S3m464a2d8kiXykpJC6MAVZehAz63h50ZKPVdNb1RpC7BRkcz8KTulk9Re7XzbmfyoiiVZWLZdxj0m5mgMSSPIjd2hC4OWfl+Q60pIFOGlJkb+90HwFOSeo3wNCeqPhQGD7ZflP6UukN7VPgf0pBnBOIVMje7oPxoBcPslrXnmX7REI/TcE5C/ClRxGRB3rkr9xeQ/HzpUiqkluFAADEYHymgEy25uonjuwrQupVogMhgeoPmK4qcHaC8MqmwXMhznvHyhB5bOfof4ceXSpHSIvU/E/WsJ04T/wA0ma6lGnU/zin5o4Oh8LWGi3azwtPPcEMoknYEqDjkAAB4dcZ99SGuZe6rBDcCGAPdXS5zDANxX5j0X8SKZFveahg310LaE/8A09q3pH3NJ1/BQPiainShSjy01heApUadGPJSikuyENNpVnemSC0im1V1AYW8KtMR/ebwHzECnGttSv8A0rmYWMR/1MDZcj+9J4f4R+NbtvZ2tjF3dtGIVPPCeJ8/eadAlPRio94BNZpY2M0kthi0toNOi2W9vHGpOTsPNj5nPMn40+ZGJ6Mg8yMmgAxgkhT5tnnVGcQi6vOJNZfWraK4nS6dbfvpDm2hB/ZmLn+zJXa25cEk1y3d5C0gp1Nmcd9f07GCqVdm8F4mO3bJYIx8S3WtDXLW6n0TUItHkeC9e3kW3kLkBZCpCnn78VXFnxpqen6Jomm3JgbVZLVp5ry+DSqkPeMsLbQQZHdVz6w8yTmpFwRxvBrl/caReLDFrEK94vcFhFcR/fXPqnOcoSSMdTzxlG6pVHyKWr6dTKF5RqtU1LV9OuqKiv4rqxW106zYw6qdogjcmNoGTDCRgx9EAgEnGT5VKuMbO07VZrfRtQii07iCwV7i1ZJu+hnjbAcI2FPVUzlQRjkCMkTXtQ0M3mjx6mq99daduKoehicr3njywFVs8+SHlzqtOH7a8PGPD9/Y2qJcxXIUIHDfs2ysp64I7ssc8iCtVVtcV+EXcYU5PVpqWdfgvXiedg58MuFay96E2tW9fl4En7Nez3TezNb3W9bu40uGhELynlFEhcEjPjuITqOowOtd7ifXeGOKtBudH/re3tLq4MZhivQ1q7srq6YWVQxUlQMgHkTiuD2vXep3Wv6ZpqrJHptuiXrBFB76QsygEn7gG7H94ZB5Yh90Hv8AUbQvPJI0e9CtzEcSB12mPB9bOQcYPQe6urifHHUuJQr5nJ7v4fjY6rzjFK3qytORyWNceIzxHbGOC8juYb1DYys0jK4DBoyTlMg55gYJHMGtZx3HB1hbanczX0Vmxne3NsiKgdi0ndOoDBvSPrFlPL0eQqztC0PR9M4S0luL5LGxnXKCa5uO4LruPdowJUMVTYuGzjGMVIrXgfSIp47mGW5eFdrxxPKGjGMEHOMkch1JFcFDh1zR1otcr75yk8Gux4ff2M1Vs5qOXnXPMlp9TPCHB1hwxFL/AFZE4lmAEs8zBpWUZwOQ2qOfgPj0qSpshBPdsuerHmT+NJDXB9QxuPMgrQpkU5khZj5qwOPpXooxUViKPV1a1StN1Ksm2+rFNIrnGFA83FZWFOoJz5g0g3cfMYYHx3KQPzrKLFKc7kb3IeVSaxWWJxGxb3npRsfOW2v7ulZYBOQdgfAA5rG2VhzYAeXj+dAZMpBxsYn3c64HEfCegcTSxS6/p0NxLENqOdyMBnONwIJGSeWcc67+4xrzQAe41gyFvBkHmVrKE5U3zQeH4BrJr2FjY6bZRWmnwRW1tGMRxQDaB48gPfzrYCSH99lXyPM0KsOOqk+ZPOm9xc4ttx/vk+iP51DbbywOHMKEkxhR4nlSDLLIB3aFVP7x6/gKUIDvDs4dx4sOQ+A8KUZGBxtDH+6agCEWJMlgSx6s45n8az6DHESgnzBwKMk+1VvgByrLNCRz2n3Y50ACHmCXYkefOgs4OFIc+WKwIy3PJRfIGlbTGvJ8D3igMEOT+0XcPJTyrErROhSZMqf3WXINZ3SsPRAx59Kyp2dUbPietAcx9F0yd9/2SCJv+59Bj8SuKWdJ7olrfUr+DyBlEij8HDVvNKjcgFPvbkKysKdc5PmDjFAc0QawnOO9tpwDkCeAqT+Kt+lLN3qsWO902KUeLW9yPo4X61uyPsbajsz/AHRg/n5VgxSSYM21h9wHl/zoDnR6zEJpJLi1voE2gbjAXHLPim4eNbMGtaZOcR31vu+6zhW/I863DJsA3IQPDBBpm4jhul2XMaGP7siZ+tAPwEGPIIIJJyPjWZvZP8prmHQ9KLb4rdYG+9buYv8AhIpP9VzAEWup3yKeX7VllH+YE/xoDrjpSZOqfNXN7rWYgAlzY3I/7yJoz+YJH8KSb7UVkAl0suEOS1vOr/8AFtoDr0j/AFw+Wub/AF5bopN1Be22OWZbZ8fmAR/GnbfVdPuZh3F7bOcYwJBn8utAdCqs147+1S0T/wC6tx+YSrTqq9U9Ptatv/F2/wDAL/KgLqooooAooooAooooAooooAooooAooooAooooAooooArnajoek6laT2mo6XYXdrcSCWaGe3SRJHGMMykYJ5DmefIVs6hdCysbi6aKeYQoX7uCMySPgZwqjmSfAVGhxvEYSg0TVjqwufsp0ofZzcBu7EuSwl7oDYQ2TJ4gdSBQHL7aYUj4DEcSKkcc0YVVGAoAIAAHQVQ/D528WcOt5anbj83A/Wr37TryDV+zN7613dzKUkUMMMvPBBHgQcgjzFULpDbeI9Aby1WzH5zoP1owj1NSF9q/wFKZgoJYgAeJrXErPIxgXIIHpNyHj+dAPv6jZ8qZSYsoEKFzjmTyUfj/ACrPcbuczGQ+R5KPwpyL2SfAUAy0JeRe/bfnPogYFbAAAwBgUlvaJ+NLoBEPqfifrSJ/a2/zn/hNc9tXjDtBZRSXtwrEFYfVQ5/ec8h9fdSH0271AZ1W52R+Fvakqo+L+s38B7qAfudXhSVoLRXvLocjFBz2n+83RfxOfdTH2G+vP7fN3UB5/ZrZyM58GfkT+GK3ILcWUKw2xiSMeqgjA+mKcL3GBmIY/utz/jQGLaO3soVhghEEY6Kq4+nj76ot+Idcv7eTUbi61S21R90kapNthtxk4jMONjADkSylvfV7CaOPJdJE8yyk/wARXHl0DQ72/a6NjbvMxJfJIRyc5LR52seZ5kVxXlGvVS9hPl7lff0Lmsoq2qcrW+huaBO17oOnXtzCbW4uLaOaWLJHdsyglefkTit4byfQY7fNhWRAg5nOfPOKi3aJxDc8O6NBJpxVrq6uUtY3kTekWQzFiARnCo2Bnriuqc1Tg5TeiOydSNGDnN6JakoCODlgrnzJxita6tbO7ljkubGG4lhOY3kjVyh9x54/Cq14c43uoeI7Gw1bUmvNPvt0azXkccDxTBdwG5AqlWwQBjOSOZq1O8CYBQg+AHOtdGvTuI81N5Rrt7mldQ56TyiKca8MjWwt5ZyQx6pGgjXvVwkibs7W5Z5ZYjHiT58o7wdwTdW/ElrrGqRfZ5bXeVUOpd2KFP3c4TDuebZzitntcmvpF0eBB/7qkeQ3UZkKCVgB3cb4IypBcleYO0ZqGaFrOoaFrE0Olyadp9lLDveCWN5IY5A3Lu41ddm7LZxy9HOCcVVXErOF6nUWJrr0+JSXUuH0+IJ1Fiotc7L4/wBl7BHP77KPLOT+dcjU59J4VsrjUpoba2R2AdoYP2kzk4AwoJZiT+vnWnwTxFJxNpL3CxC2uLeZra4UP3iBwAfRJAJBVlPh1xzxSeOeF34h0yCOOQG5trhbmMuxUMQrKQTg45OSMDqBVtOpmk6lNczxleJd1KuaLq0lzPGV4mimsaTxdeJpeo6Xc2l6IzLEl0oEhTI3GN42IB6ZXcG5cxyqUaXp1hpVv3NlAsK9SSObHGMknqcAc/dUA4Q4PvbfiGz1S+hkh+wmRo0aZXLMyFPAkbcM3jnIHKpP2h2l5qXBmp2ti7i5lRQVUH0o94MigY5kpuGPHNaLepOdN1qlPllrp1wc1pVnUpO4rUuWeunXCK24pv43491i8tNT0+4GyKCNkZZe4TbhoiR6pLiQlepyKnfZXpN5p3Dc0V6Giha7kktYdu0RRHHIKRyG/eR7mFQHQ7O+v+INEWxEQk066T2UO0wQg/tEJA9EFAwwcZJFTntI4ivdEfS7LT3NtJfGRnuAneGKNAudqk43kuuM5Awcg1wWdSLlO8lKSj2ey2K2wqwlKpfznJR7S0S2JszMpwGDnyxQRIT6a5XyU1XvZ9xVfXuu3OkXlw13ELY3UFzNCscgCsqsj7MKT6akEKPHOasLfKw5IAPP/lVvRrQrw56byi9oXFO4gqlJ5TM94iAAgr5DFNssc55rH+IBb/lTilVOSr58yM1hpEc7VCsff0rabhP2aNBlGdPMhzWAJif2Uu4ebqP0xSxAv73X3cgKxI/dnaHZnPRMZNAJAmU5ZEkPmGwfyxSWvMZAhkLjqAMgfEjNKKTSAd5gL4opxn4mnAyxIB3exR5YxQDCNFIwM8qlvBPVA/A9afYRqBjIJ6BTSWkD5U4Vf7woW2gxlUA96nB/hQGdkjDm5UeXU1n0o1/c2j8Kb2Nn9jLJ+JBH8aO7nDZLxyHw3AjFAL7x2xhCo8+v8KFMY69T1LCkmd1OGhJP9xgf5Unvlb225B90qQPzoBZCMcRqCfMHArIhPIl2JHnzFYDW7DKtGR7iKyELH0SyL8ef/KgMszqcAqx8sc6wd5P7RSV8lNZVGQeiw/EU330j5EKq2P388v8AnQDjSog9PKj3imQPtB9HbGvny3H+VLjVUbfIHaT7zDOPhjpSnkjPLAY+VAZWFUB2Er4nBrAMhP7NgR5kUCEH1uXuU8qywKDPeED3jNAChlOSoY+eaDNjI2Nu8sVj9qw6AD8iaUrbBjuyB7udAIAjc5dlLeXTFKZUUDBYZ6AHrSWlVuQxg+LdKUkUfUcz5g/yoDGyRhzcgeRH8qV6SL0TaPI4pLZU4RmLeXWjZISCxVvcRyFABkZhyVlHnjNMz21lcDFzBDL/ALZAfrWlxJxHpvDWnm81q4SCLOEUHc8rfdRB6TH3AGqd4k411XjCLbbPJpWgyjKxQyft7pCORkdfUUj91D8WPSgJLxhxXomlXE+n8L2xvNXQlJGtrh4be1bH+sZTgkfcXJ89vWon2Z31/qfGkMmrXRu7qPUQhlK7cgKp6c8Drj+JJ5nS4L4avriKPTdPg75lkkI2DCRozsVBPgACB+FXR2ednNpwrJPeXMwvNRmlabdjCREgDC+fTqfyFAT2iolqNxfWnaHY95qDnT5NLvJBZgKkatG9vh2J5lvTfmSABjAByWgOjXOoW1hY6drT3lnfastnLPdQcRz3u6GSUK2CcLbszMFBiyCGO18qDRatJdfy19iZe6ssuuiqjEpub7UNOu9b1G30zSIb2W0uE1GVHcxNGC0km7dKIizIQ5YffBOKs/Qrie70TT7i8j7u6mt45JU+65UFh+eaLWPN61z+DF6Plfj9Mfk3aKKKEhRRRQBRRRQBRRRQBRRRQBRRRQGvqAujYzjTmgW82HujOpaPd4bgCDj4VALHhbX7C8bWLGz0S1vBdmZdIiu5BaBWjKOwlEIKyMx3kiLBxg8yWqx6KjAK2460abTux66sJbrF2oEss8CgDvXl3uVDA8tzNgHwrzxpUWoQa/oJkvYpoRq1jnfBhx/pMfiGx/CvUnaqM8Aav8if8a15jdtlxYyfcvbZ/wApkP6VL1C0PViwLkNITI3m3QfAUse2b5R+tLpskCUknA20A5SIfZJ8ormvrCzO0WlQteyA4LqdsSn3v0/AZNNDS7i6A/rabv4x/wDTwkpF+Pi34nHuoByfV43m7vTonvpkOG7r1F+Z+g+AyfdTYsZb3nq91uQ//TQExx/ifWb+A91dONooEWNI+7VR6KKuAB7gKyG7zluCjyzk0AlIreGNY4o40ReSoigY+AFKCMTyLIPLOTWe7jUZwB784pIDH2bMB5tQGQpjBIZfeWH60d5IR6Mf45oEbg5JVz7+VHfHJGwkjy50AAqDl927zYUOY5PR2rIfLAIrG4N7Rsf3elKbutoyFx4YFAcLW9c0bRJ0g1G7eO4kTeLe2jkmfZz9MpGGIXkfSIxyp2WLTuI9EQw3cd7p8+GjeNgwJB6qy4OQRj8wfGoJxhw/qsHFOoapaLeyQXvdbTboZDHtQLsIGSBlS2cY9KpT2c6HeaFot0L19slzdPc92+CYwQoxkHHMqW/xVwwuJVa0qE6bwur2ZW07uVe4nbTpNRXVrR/2VpqmlX2mapdWd/scSSSRQCaLcJoWI2gDGGO3bnGTnNWh2fQXWk8G6ba6qsomiRhll5rHuJjU+IITaMEcsVIRPI4PdIGH3s8v+dCouQ0+92HTcOQ+A6VFpYK1nKUZPD2XREWPDI2dSU4SbT2WmF5YGp5obyN4CsMkbjDCYAqR5bT1qM6twDZXUwm06WOxdgA6rbqY2x4hRtwenjjkOVS9njYY5OT4dabFqhOdoT3Rnb9K6a1vTrx5Ksco7Li1o3MOStFSXiQe21zRuEzdaXpltqV81vIZL6a2iQrG5APpZK7yFwMIGIC4PMVMtOu4tU0+3vbOdJ7WdBJGwBUMD8ef4HpVa6vwHfW2r3clgjT213cvcCQThShdtzbgcdCTjG44Aqb8H6NPw/w5aabGY3EW9mJJHpO7OwHLoCxAyByxXNaVKrnKlKnyxjt9sfA47GrWdSVGVLkhHRPo+2Pgd0ybMBkx5bTmsGTceZMY9450lXKc3hfPiww3/Osfa4jyVgD/AH/RH8a7yzHAkWM4U+/r/GuZrei2mt2yw3CyAIdySo5UocYyPPr0PKuksSP6TYc+7pWWCryDOD4AHNYzhGcXGSymYzhGpFwmspnI0Hhy00Te1qzyzuAHmm5sQCSBywB18AK65kYHbtDH+6axtlYc2wPL/nWS3dISyqFHiD/Oop04048sFhGNOlClFQprCXRCclvahgPIDlWXkhC+kVIHhjJ/KkNM747tSin99lP8BSoo4uuQ7nqzHJrM2CBG8hBAMKe71j+gpxIRGDsbGeZyAc0EJnEYOf7pwBR3TEDc+T5EcqAA8jZ2BWH3ugoXKnLoxbz61lmZOu0+QHI1gs7H0lZV93M0BlpkHLx8jyrAiV+bBfgtKV41GAQvx5UkhX9RR81AZKhB67KPjmsYlYdQB7xzrIhAOQ7bvM86wzOpwGDnyxQGVyg9n+IP86wZs+qCPeRyoIcn9ou4eSnlWWmRB6eVHvFAJEUMhywSRvM4NNyJFG22PvO8+6jH/wBBWcm55eiifgWP8qdWBEGEBX4E0Ax9nmcDvZgR9wrkfjjGacLzRr6SRlfcxH8MUrLE4jYt7yOVAV1OSFc+ecUAgzOfWikRfMDJ/hSlmt8bdyj3NyP8aUZdpwUbPkOdJysntGAH3TyoAwjeyUfMDgfwpQiIOd7FvM86SYIMbtir715fSkiJyf2csqL5sc5/OgHGZ1OMqx8sYNYO8nMiEjyB5UlY5o/VaNvipBP45rBmlBI7ncR9xsj+OKAd71APSyvxFIAWU5UKB5jqaSsqA5l3hv7yHA/SuTxRxTonDlktxqt0gaQlYYIx3ks7AZ2og5k/wHiQKA7YiC+oWX4Gqu487WINIt7uPhhI9VubcHvblv7NCR1G4Ed4w+6px5stQnjbinX+KGgh2vp2iyzKslhDITI8eCSZpAeYPIbF9Hnglq2NB4eudZlWx02zV4wACoUCNF9/gBQHMmjnvr177VrqbUNRdShuJsZVT+7Go5IvuX8cnnU74D7NLi4s7X7f3lpp0Maoit7WRQABjy+J/Kp/whwHY6IEuLzbd3457iPQQ/3Qfqf4VMqA09K0yz0m0W20+BIYh4KObHzJ6k1uUUUA01vC1zHcNDGbiNWRJSo3KrEFgD1AJVcjx2jyrmW/C+gW1rfWttoelQ21+SbuKO0jVLj/AGgAw/U9c9a7FFAcmbhnQZ7GysptE0ySzsWD2sD2kZjt2HQxqRhSPMYrrUUUAUUUUAUUUUAUUUUAUUUUAUUUUAUUUUAmQMY2EbKrkHaWGQD4ZGRn86rVL7X4Td2kHEc+oW011bWK6m9pArQzl2FwIQqBGCgKBuD7XJBLlWUWTPEs8EkUm7ZIpVtrFTgjHIjmPiKjdhwJoNjo8ulwR6g1g6xosM2p3UohEZyhiLyExFSAQU2kYHkKLf5E9CO8T6hN/wCzTiiLVLmW6bTpzbG6aMbplDRsGKooGcOAdoAypOBXnCTU7K4iBtruCV0kR9quCww4PMdR0r1XxRpNppPZ5qljp0bRwLC7+lI0jsxbczM7EszEkksSSSeZryjxPDE+jXcjxozpGSGKgkVJij1e2rG5Yx6RAbxgcGXO2FT738fguaSdIe8IfVrg3B69yg2wj3berf4ifgK802Et3pnLStS1KwXOQltdyJHn/Z52H8RXat+0rjHTr61tf60gvllRzm+tUJG3HLMXdnx6+7xqCT0aP2KqiBMAYVFGMD8KyWkPrKVH93BNU5p/bDqEC41Lh2GYA85LK7wzf4JFA/z1ItP7YuF7pmjuGv8AT5EbawubVnCnAOC0W9RyIPMjrQFhK0aD7vxGKCe99VQR5sK5Gi8S6BrTAaVrWnX8p/chuUdh/hByPyrrsI84C5b+7QAIFGMk586wSwOEcsfIjNAiYjm7AeQOayd0a9Ux8MUBgiQ+uAR5KcVnvFQAFSg8OX8qwXkP7hUefX+FZVo1OSSG825GgMCTvOSkKPf1/KlCKMDp+PjSHlDnbEnenz/dHxNYW2yD3pzn90clFAY3lji3LN/eJ9Efiev4UGBmbdIwk8lPID8KcbKAAP8AAEZrB71hzAA9x50BkylThkOfJTmk793rkoPLp/GlKyoOaMvmcZo74McRkH3k0BnEezou2kbd3swVHnk/SlCFScsNzefShgFOFZ93kDn60ACIhtwfJ/vDNYMjhtoUOfcaNsrD0mGPL/nWdxjXmgCjyNAJyT7UNjyA5fwpfeR4xuHw/wCVJMueQyg82FKVUPPIc+Z50A0bdJDnu1T3gYY0oW+zJjlkXz55+tYdkDbYlLP5IcAfE+FY7h3Ud8+eedvh+PnQCBLOzYhKSj7xUgD8c8/woVZAwaeJpHHipBA+A5U+WZBz2Y93KsF3PVWRfMDJoBLXcS8nLKfJlIrK7Z+ZKFfJTn+NLRo15AgE+fU026RSHlEjn72On40A4Y0UZBKgeRxSR3jeox2+bCki1Awe8kB+bIHwBzQ3ex9JVbyDLzP5UAtVZOe0MfPPOsGbGRsYkeXOkFpz68Xo+SNz/jilCdEGGR4x71OPzHKgMgo5/aOCfu9BSnWMDJAHw60gTJMdsTI3vJ/SlLAg54OfMHFAYCO3RmRfLOTWVVkGFK494xSJH2NtR2Zz0Uc//SsGKSTBm2kfcBwPx86AO/dwRCgYjluzy/51mMIrb5CzSfecdPh5U4X2D0kIA8sYpJl3HGdg8zyNAZZo2+65PgOdYEOfWJUfdB5UoRxkdA3v60kgA4j3bvceQoBRUovKTAH3hSd0rD0QMefSju3yCXDEeY5VlnZBlgD8DQApCfuMD4nrmhpk9UEFvI8qwWZj6QZF9w5mlK0eNoK/CgErCh9JgCfdyrLAIM72H45rBVWP7NRn7w5CsiLByHbd5nnQGMSsOZAHl0JrJcxoSyBUUZJBGAK4HFvF2mcKwIdRn7y6l9jZwLunm+VM9PNjhR4kVTGt8T6lx1D3moyC20ZywTTIGOyQBjzmbkZDy9XkvuPWgJtxR2ppNLNp/Bghu509GXUZedvCf7gHOVuvQhfeelVXIs8nGcFxd3VxeXs9nM008zbmkIeLHIclA54UAAZOBUh4W4VvdT1S6GlxNJ37IzHG1IgFC8z+FXVwl2faXodzFf3CLd6qiFFnYcowSCQo+KjmefLwoCEcL8ATXSR3uvSiwsSyhVchXkLEBRz6ZJAGeZ5YHOrS0y40HSr1OH7G60+C/EfeixWZe/KffKZ3EcvWrm9oukpqemafILR7q5tdSspogql+7xdRF3CjlkIG9LGQpbmATmN6ra3k2pahpFrYXyancauL+O9Fs4gEPdKN5nxtztUxbc7+fq7edR0z66flv4E40z69dPNk5h4l0Ke0vrqHWtMktrBit3Ml1GUtyOokYHCEe/Fb9he2uo2cN3p9zBdWky7o5oJA6OPNWHIj4VUqxTXMWj3VvomqQ2Wi21lDfW76e6M7Ryq22OPGZe62s2YwwO70Cx5VPuB1ley1G7eC4tre8v5bi3huIjFIsZwMlGwy7mDPggH0+YB5VnjfXv8Ab+d15dTFt9vWM/TZ+ZI6KKKxJCiiigCiiigCiiigCiiigCiiigCiiigCiiigCiiigCiiigONxNq0Om28EL6ddapPeOYYrK2WMvLhSzZ7xlQKFBJLMB0HMkAx284H4R4x0Ey/1d3MN7CV3w5ikTPIjHQMDkdDzFdziiw1Ka40zUNESzmvbGV27i7maGOVHQqRvVHKkZBHonOCOWcja4W0yTR9BtbO4kSW4XdJM8YIVpHYu5UHmBuY491F1D3IHqPY5pcvOwv7m3PlIBJ/KorqXY7rELGSzntLrbkIM7Wx+IwPzq+6KA8u6jwRxFp5P2jSrgqOZaNd6j8RyqNLYNZzXLtHKjTyd4+8eIVV5fgor2PWteafZ3q4vLS3uB/3sYb60B47vbO3u4itxBFLy5d4gbB/GnNBuNW0ywtha6tqdlOI17xYLtxGHxz/AGeSnXP7tem9S7OuGb7cW08Qu3V4XKn8un8Ki+o9jVhISdP1KeHyWVA+fxGPpQFXjtO4w0hYmfUrTUUkkSL/AE2zXcCxwCDEYx1PiDUq07thu4iv9bcOCTHJpbG8DsfeEkVQPhvNN6n2Qa7Ev+jtaXgByAH2nlzB9LHOoxqXCGv6duN1pdyqL1cISv5jlQFmWnbDwrK3d3Ul9YXBG4R3Vq2MeJLpuUAfGpRo2vaLr+P6t1rT9QON3dWtyj4HvAOfzry7cxvFxJaiRGUm0l5EY6PH/Oti5srW6wbm2hmI6GRA2PhmgPWTJEo5qq/DlWArk+izIvv5mvKGh6jrWn3N8LLWNXs445wsCrcuYwndofRRsoRuLeHu8KmFh2kcYWR9O/sdQTxF5ZgN+DRFAP8AdNAegFRk6bW8yeRrHek52oSR4g5FUzoXbXNd2lvcarw5KYZUDA2N0rnB80kCAfDcalun9rXClwALm4u9OfxW7tJFUfF1BT/NQE5BUn9o3PyIwKWzJgZwfIda5mka/pWuLnR9UsLxcZJt7hJTj4KTiukIUHhz8/GgEiLceWYx5A86yIyg9F8fEZrB64jZifjkD86Cjk5Yq/u6CgAPIc7VVvf0FA5HMiuW88ZA/KsvKIwO8XbnkMEGmzI8hIz3KeZ9Y/oKAcedFHUk+Cgc6b7ppjmUBF+6vX8T/KnY4o1U7QDnqTzJ+JpJC5xGvPzBwBQGREqL6BKAeR5VgGQn0CCvmwo7puRL5I8xkVlnZB6W0/A4NAYUMpyybm8way0yjIIbd5YrBdyfSVkX3DJpSNGOSkCgMDEnrMCPug1lkjUZwF945VhtrnCqGPmegoEI5Escj+FAYAdj6DMq+bc6yqOnTax8zyNDFk/fB8gRzP5Vg94wG5cDyU86AyZSCRsJb3c6wCpOZW5+RGBSg6qMbWUfCmzNvbZAAx8WboP50AubuSm6UIV6cxmmFgLnMe+BPcxyfw6CnUt0Xm2Wc+PT8vKlMAnR2B8B1oBEcDxDEUv++oOfxGKx3s4JAjST3q2Pr/Ol7ZWHpEY8ulKDFRgx4A+6aAaEmDmaOUN8uQPyzS/tMJ5d4ufLx/KgzA428h95hyrISNhz2vnxPOgMd2HOSoUe7qaUIwo9BmUfHNNtDCvqqVJ6BCR9Kx3EpHOZgPukA0AvdIThCre8jlQoZTlkLN5g5rGZ0HSJwPIlf50k3DkeycD7wG4fhigHGmVfW3A+RFYGJfWKkfdBpKTQA+uAx+/yJ/Oo9xlxnpHDUYjuSbvUpULQWFuA0snvPgi/3mIHLxPKgJHN3MELyyssUSKWdy21VA5kk+Aqn+Ou1mSOxuRwYomhjHpanOuYjnl+xU83PP1z6Plv6VEOKdY1zijVrQawyrpJZ3/q6AkwxYA2d4eRlbPiQBkclHj2NC4cvuIZ/s1lbCRP33cfs1HvNAca3tcXEs8jzXV9OQZbmdjJLKfDLHw8gOQ8AKsTgfsyklhil1RGsrJfSS3HruOvP7o/jU84S4I0/QAk0gF1fjn3zjknyjw+PX4VLKA1tOsLXTbRLaxgSCBeioP4nzPvNbNFFAFFFFAFFFFAFFFFAFFFFAFFFFAFFFFAFFFFAFFFFAFFFFAFFFFAFFFFAFFFFAFFFFAFFFFAFFFFAFFFFAQftB4rudD1PTLCyu4LR7iGe5lll0m51HakZjGdkDKVGZObsdox76zDxLqj6n9q7zTpNBF/Hpu2OJzM7uq4mEm/aFLuBs2nlz3eFd3iLQX1nZ3esarpnoNFILKRAJUbqpDowB/vKFYeDVo2nBVhaapBcW11fR2MMizppgdfswlWMRrJzXfkKB6O/bkbtu7nSO+vrX8aefzEtVp69P6fI7N9o2mahKJb7TrS4lVSqySQqzAHGQCRkZwPyFRvUezThm9BxZPbMerQSEH+ORUzooCpNS7GbZtzadqcifdSaPI/3h/KotqPZNxFbc7cW12POOTH/FivQlFAeT7rhLV9GgWObSrqCCMbVPdnaAPI1wdXs5Lmxmt/Zu4GCwPLmDXs6udf6Hpeobvtmn2sxYYLNEN359aA8h3Fja3Lq9xbQyuvNWdASPgfCnV1rW9Gn06LSNb1W2jknMZX7U8qIvdu3KOQsg5qP3cczXpDUey/hm85x20tqf8AuZD+uai2pdjKnc2narzPRJo8AfiM/SgINp3aVxfYgK91p2oRj/8AirTY5/xRsqj/AHDXetO2xxcJbalw9KkpTeWsblZsDpnEgj8fDJ/GtLUeyviS0JMMMN0gHrRSD6HBqD6lw3rWna8kt7pd3DF9mZN7xEDO8cs0BdOmdqfCExBur25sZycE39tJGB/+kwYwPg1THTNb0vV4y+kajZ6gnnazrKPzUmvMTKVOGBB8iK5o0uF764uLmOKUuytESuWjwoBwfDmCeVAeuu5DHLgD3L/OlbNg9FyoHn0ry/Yavrem7f6t1/V7YL6qm5MyD3BJdygfhXY0LtU4t7p3nfTL9I5pI8XFuUc7HK+sjBRnGfU5ZoD0MGlbOzaR5kYrK5XmyMT97Oaqew7ZsEDVuG7qP+9Y3KTgfHf3Z/LNd7Te1nhDUIkdtVNijgENdwPEuD0PeEbMe8MaAnTToOWTnyIxRt7zm5BH3R0rW0nU9N1SAy6TfWl7COr20yyj8SpNbDBCcIgLeY5Y/GgFGNAM42+8HFJG9vZswXzYUCE8iXYkfiP41mR2iXc7Jj38qAFV054Vj55waS84U7djF8Z2jBNJLyyY9Fo0PiObH+VLi7qMYX0fPPU/nQDYAlP7dxj/ALMch+PnT7Km30guB51hnB5KN5/hSRAp5t193ICgMBd3s8qPPJ+lKWNlJKtkn7wzWWBUZ7wge/nScysOWAPPoTQGTIynBUMfJTSc55yhgPLHKlKdgx3bD39c0GZAcA5by6UAoSJjky/nSCok9VQB94j6UoR7ucmG93hQURRnJUe44oDAiC81ZgfPNDM6nAYMfLHOsASN6rkL5sKyoZByVT5kHmaAxhycyLuHgFPKkXd7bWVtJcXsyW1vGNzyzEIiDzLHkBUW4z7QdJ4YlSycm81mXlFp8LrvJwSC5zhFwCcnmQDgHFVDxJfatxUzS8QXSOAMwWUGRbQNjk2Dzdx95vwC9KAl3FHaXd6sHtOEUa2smBV9Vnj9Nv8AYRsP87jHkp61XHD8BGq62qmWaVrpA0kjF5JCYY2JZjzJyx/9KlPBfCuparBa2VlFuWCNI5JzkRrgAZJ/TrVy8FcAaVwvLcXaBrnULmQSyTS4IVgip6A8BhR5nrz8KAiHCHZvPd7LrXd1vByIgHKRvm+6P4/CrYsLK20+1S2soUhgToiDA/8AX31UWrNFB2l6jcp/0ZvtcmulhtLQ2TNqsEf2dV71JWI2opDNyQqQT6eTgc23bh42FsulfY/6hFvaHiTYPQ73vVz9qP3/AGne7/S243+jSPvY+H19a/IS0yXvRUU7OGtm0a7Old1/Un22Uab3IxH3HL2eOWzf3m3HLbjHLFSupITCiiioJCiiigCiiigCiiigCiiigCiiigCiiigCiiigCiiigCiiigCiiigCiiigCiiigCiiigCiiigCiiigCiiigCiiigCiiigCiiigCiiigNbUoriexmitLk2kzjAnCB2TzKg8t2M4yCAcEgjkavs7qXVOHeHG1fWr+2EfDf8AWbTxXjwNJMqx5lkKkbwuclTlfT9IHli2a5l5w9ot7a2dteaRp1xbWRVrWKW2R0gKjClARhSB0xjFR39dGvun8DJNJar1/vYr7RtQvbm4tNZu728TWJNUgsHsPtTiFY2hRnTuM7NwVml3Fd3Lrt5VahGRg9K0Do2mHWBqx02y/rUR90L3uF77Z93fjdj3ZxW/WTenrw/v4mtLHX1r/XwOTqHDmjagGF5plpIW6t3YDH8RzqMaj2VcN3RJhjuLU+AikyPyOfrU9oqDIpnUexiUAnTtVRz5TxlcfiM1Fb/su4jsA/c2Uc8YJbMDg7ieZO3r/CvSFFAeSr/RtS09tt7YXMDeTxkVx9NtDYada2hbeYIki3Yxu2gDOPDpXsxlDKVYAqeoI61xdQ4U0HUFIutKtGz1KpsJ/FcUB5B1qxiaxvLi3tYzfrC5hkWMGQNtOMHr1xUg07W9f00L/V3EWrwYGNslx9pUDy2zBwB8KvfUuybh+53NbG5tXPQK+5R+B5/xqLaj2M3ac9P1OGUeUyFD/DNAQ8drPFWk23eXf9WalGHVR3lu0UhLMFGWVtvUj9ypLpvbBEr51jh29V8e0s7iO4VfwbuyPwBqI8X9mfFNtpzCPTXusTwkfZyJCQJVJOBzxjnXKvdLvrKQpd2c8LjwdCKAuuw7VOD7pV73VfsLHqL+GS3Cny3OAp/AkVKtP1C01aDvtPvLe5t/v28qyA/iCRXlS/tmuPs4VgvdzLIc+IHhWWsLUzd8LeNZ/wDtUG1x/iHOgPWvdJ4KB8OVIOc4jZifjkCvLScTcS6TdWEWmcQ6qkc0hjdZpvtIChGYe1D45qOlS7Tu1LiuzVVuY9J1GNfBont3b4srMv5JQF7hHDbiVc+/lilGQqMupA8wc1U1p212qyRw6roN7bzSAlTazRzpy69SjePgtSXTe07g68Kd5rMdnI3hqEb2oB8syAL+RNATLvNxwT3Y9/ImnFVduFAxTFnf2d9ai4srqC5t25CSGQOp+BHKl93vOduwe7kTQAypnCL6X93ligRHkS5JHnzFKEe0egzKPLrUF4/7StO4SiuoYl/rPU4IjK9rAcCFQM5lfmE5c8c2PgDQEx1TULfSdPnvtSube2s4F3STStsVR7yap/iPtNveIZLmx4VaTTrGJu7mvpExPLlQf2SMP2YwQdzDdz5KOtRzVLzUeILyO+4iuhdzRndDAi7Le3+RPE/32y3vA5V0uEuEL3Wb+6bTom2Tyh5ppDhEIRV6/BRy5mgI6mjRtc2Jtg3eRXBnbOXed2jdMsxOSx35ycnlVtcIdm0tzsutf3QwnmLYHDt8x8B7uvwqb8KcHadw8iyIv2i9x6U8g5j5R+79aktAM2drb2VukFpCkMKDCogwBT1FFAFFFFAFFFFAaGvakNH0W91JrW6u1tYmmaC1UNK4AyQoJAJx4ZrlaBxlpfEGrfYtG767QWMV893GFMKLL7NCc53kAtgDkBzIyMySoJwZwRcaBoGr6fBerpU17qtxfJcaXHEWWN5MopEsTLkLhT6JxjkaLfX16zn4eIe2nr1jHx8Dq6zxrpOkcY6Nw1dmc6jqqu0RRQY48A47w5yu7awXkclTXUm13SYpZIX1OxE6TC3MRuEDiUpvEeCeTlfSweeOfSq24l7Mtd1q817VxxA0GsSTW7aaiCPudtvhoe+Yw94pLmRmEZA9PoelbN7wFrVx2oNxgp0dWaEWDWxLewMTAzb9me+DttAxjZkZ58o15fH1j8P5k6Z8PWf9fImdhxfod1FpXe6nYWt1qcay2tpNewGWUHps2OwfyyhYeRrv1RadkWuxRcIrBdadDcaXa2cF1cRXMuHMEhYhoWjaOdRklMiJlbnk8gL0rJ41838uhis/Rf7CiiioJCiiigCiiigCiiigCiiigCiiigCiiigCiiigCiiigCiiigCiiigCiiigCiiigCiiigCiiigCiiigCiiigCiiqL0/W7z/ANtcmjPr2pycKQXc09u4aRu9vhGGeyMu7LogLOI8Hn6PPbii1ePXr+uoe2fXr++helFVB2u8V3Gp6LpWkcMXWt6de6nJJK88OmXi3UMMK5LCIR96A0hiTO3BDNzpjiLtZ1Cx4O4R1zTYNPZdZVrW4ivA6taXAGGlfafZRsriQEA4xzFFr8/X4D0aLmoqldc464i0i44mXSLS3vry31iK02L3lw7p9jWVjDbPcLvbP7kbLhcthiCTaHBOtHiLhHSNXYw77y2SV+5DhA5HpBd4DYznqM0Wqz5fVZIzrjz+jwdqiiihIUUUUAUUUUBV+oS64dK4ssUv5L+/OtWtrCXvBp4VJI7ZnjjkX0o1w7427n5/vN10be4jvO90+8vtR0mPSbS8mkEWuXE4+0RumZPtDkPMiBh6L+iCxDLyGLRutK067t7y3u7C0ngvDm5jlhVlnOAuXBGG5Ko555AeVasnDGgS2NlZS6Hpb2Vk/eWtu1pGY4G+8i4wp5nmMVH4+2Ppv59jJvL9etdvI2tCuJ7vRNPuLyPu7qa3jklT7rlQWH55rbljSVCkqK6HqrDINKorKTy20YRWEkzgahwbw9qA/wBJ0m2z5xr3f/DiotqXZFodwGNnPdWrnpzDqPw5fWrIoqCSj9R7G9QjJNhqNvMo8JAUY/UfxqLaj2e8TWIy+mSSjzhIk+lemaKA8e32kzwXscl3bTxTQBgAykY3Yzn8qRXsG4t4bmPu7mGOVPuyKGH5Go/qPA/Dl+SZ9KgVvOLKY/AcqA8lPpyLrUFxbwLCvcyd5NDiN9+5NnpLhum/p/KpPYcScS6cR9h4k1RV8VuJBdA/jMGP5EVcuo9j2jzA/Yby6tmP38SD9Ki+pdjurQ7msby2uFHRWyjH8+X8aAh8/aLxVq0y6Fc6lBbb4Wna6sbcwzsisFKbi7Bc7hzVQeXIjrWpDpFtJZSabBbZhuA0bRJnMm/kckcyTnr1rqaV2Z8THtCt47iwaC3/AKvkD3Tc4lPeJy3Dlu5Hl1q1orBODLqG20PSYtW1L7M93c3FxcdwUiUgER4R8uSTheQ5HLDlmM4JSyczhDs1eUR3XEGY4+q2qnDH5j4fDr8KtS0tobS3SC1iSKFBhUQYApNjdRX1lb3ds26CeNZY281YZB/I0/WTWHhmKaaygoooqCQooooAooooAooooAooooAooooAooooAooooAooooAooooAooooAooooAooooAooooAooooAooooAooooAooooAooooAooooAooooAooooAooooAooooArmpoGjpaxWyaTp620U/wBqjiFsgRJt27vAMYD5JO7rnnXSop4gY+xWv28X32aD7aI+5+0d2O87vOdm7rtzzx0zWj/0b0PEg/qbTcSJLG/+ip6SyndIp5cw55sPE8zmurRQHHuOFuH7iyms7jQtKltJmR5YHs42SRkUKpZSMEhQACegAFdS2ghtbeK3too4YIlCRxxqFVFAwAAOQAHhTlFBgKKKKAKKKKAKKKKAKKKKAKKKKAKKKKAKKKKAK43F/wBj/qKY6lfXllaBk3vZytHNJ6QxGhT08scKAmGOcA5NdmtLWNJ07WrI2es6faahaFgxgu4VlQkdDtYEZqGSit3tLuGGCx13WNVsYrXTrzUoQdRdJYwJQU76RWzKYkZQQzMpJ9LfyNZ0bUL25uLTWbu9vE1iTVILB7D7U4hWNoUZ07jOzcFZpdxXdy67eVTr/onw79gtLH+oNI+xWknfW1v9jj7uGTOd6LtwrZJ5jnW2dG0w6wNWOm2X9aiPuhe9wvfbPu78bse7OKyTw8+t8/xp5fIxksrtv/GPpuvE36jfFHD9/qd2l1pGqpps7W8lnO0lr3+6JyDlPSXbICOTHcvM5VuWJJRWOMmSeBixtYrGyt7S2XbBBGsUa+SqMAfkKfoorJvLyzFJJYQUUUVBIUUUUAUUUUAUUUUAUUUUAUUUUAUUUUAUUUUAUUUUAUUUUAUUUUAUUUUAUUUUAUUUUB//2Q==)

# + [markdown] id="GcrQ8dn74Gzk"
# ## Convert data to numerical values

# + id="AHOBZ9tBuymS"
# Create new columns for each skill
for skill in skills:
    mentor_df[skill] = 0
    mentee_df[skill] = 0

# Create new columns for time zones
for time in time_zones:
    mentor_df[time] = 0
    mentee_df[time] = 0

# Create new columns for purpose
for i in purpose:
    mentor_df[i] = 0
    mentee_df[i] = 0

# + colab={"base_uri": "https://localhost:8080/", "height": 197} id="nHpMJVYB08D4" outputId="b831fcb3-f031-4571-9be1-c3f0b73ddfc9"
mentor_df.head(1)

# + [markdown] id="6lIE_YGz3xqQ"
# ## Transform Mentor dataframe

# + id="IC7V0pHJyluo"
for i in range(len(mentor_df)):

    # OHE skills
    for skill in skills:
        if skill in mentor_df.loc[i, 'skills']:
            mentor_df.loc[i, skill] = 1

    # OHE time zone
    for time in time_zones:
        if time in mentor_df.loc[i, 'time_zone']:
            mentor_df.loc[i, time] = 1

    # OHE 'technical' vs 'career preparation'
    mentor_df['Technical'] = 1
    if mentor_df.loc[i, 'career_capable']:
        mentor_df.loc[i, 'Career Preparation'] = 1

# + colab={"base_uri": "https://localhost:8080/", "height": 346} id="HcJ_JALT4QpA" outputId="5dc31817-746f-44aa-c80d-8aa1c6e21ee7"
mentor_df.head(3)

# + [markdown] id="pHltNPo2303k"
# ## Transform Mentee dataframe

# + id="imS4F3Nwz5U3"
for i in range(len(mentee_df)):

    # OHE skills
    for skill in skills:
        if skill in mentee_df.loc[i, 'desired_skills']:
            mentee_df.loc[i, skill] = 1

    # OHE time zone
    for time in time_zones:
        if time in mentee_df.loc[i, 'time_zone']:
            mentee_df.loc[i, time] = 1

    # OHE purpose
    for j in purpose:
        if j in mentee_df.loc[i, 'tech_or_career']:
            mentee_df.loc[i, j] = 1

# + colab={"base_uri": "https://localhost:8080/", "height": 311} id="FHroxeO14V0r" outputId="d7a3a690-5178-488b-b73f-a8849eacfdb7"
mentee_df.head(3)

# + [markdown] id="vFhaEn-MZcRj"
# ## Create euclidean distance function

# + id="KRe4GTQMTeJY"
import numpy as np


def euclidian_distance(point1, point2):
    point1 = np.array(point1)
    point2 = np.array(point2)
    dist = np.linalg.norm(point1 - point2)
    return dist


# Add 'euc_dist' and 'mentee_suggestions' column

mentee_df['euc_dist'] = ''

# + [markdown] id="k7WlLwvvkqYl"
# ## Reduce Mentor and Mentee dataframes to skills only, so they can be compared against each other

# + colab={"base_uri": "https://localhost:8080/", "height": 81} id="G-qI5XyIXMpT" outputId="df2f6430-c403-482a-e14c-f49bfe2b26a8"
mentor_df_skills_only = mentor_df[[
    'HTML',
    'CSS',
    'JavaScript',
    'Python',
    'Ruby',
    'C++',
    'Axios',
    'React',
    'Node.JS',
    'C#',
    'Django',
    'MongoDB',
    'SQL',
    'PostgreSQL',
    'NoSQL',
    'PHP',
    'Angular',
    'Microsoft Azure',
    'IOS',
    'Android',
    ]]

mentor_df_skills_only.head(1)

# + colab={"base_uri": "https://localhost:8080/", "height": 81} id="dRplgeaXWsh3" outputId="91859d24-c50f-4ba7-9667-d90811e3dc80"
mentee_df_skills_only = mentee_df[[
    'HTML',
    'CSS',
    'JavaScript',
    'Python',
    'Ruby',
    'C++',
    'Axios',
    'React',
    'Node.JS',
    'C#',
    'Django',
    'MongoDB',
    'SQL',
    'PostgreSQL',
    'NoSQL',
    'PHP',
    'Angular',
    'Microsoft Azure',
    'IOS',
    'Android',
    ]]

mentee_df_skills_only.head(1)

# + [markdown] id="Rk6cRuvWeLpV"
# ## Create columns for mentee recommendations

# + id="kYe1z9B3eKlN"
mentor_df['mentee_rec_1'] = ''
mentor_df['mentee_rec_2'] = ''
mentor_df['mentee_rec_3'] = ''
mentor_df['mentee_rec_4'] = ''
mentor_df['mentee_rec_5'] = ''

# + colab={"base_uri": "https://localhost:8080/", "height": 197} id="hOSVL-TqQik8" outputId="10b91e19-ca38-4e32-dead-6fcb31c9b893"
mentor_df.head(1)

# + [markdown] id="G28nHwJLeUgZ"
# ## Find top 5 mentees for each mentor
#
#

# + [markdown] id="qZ0iM34kOVlZ"
# * Warning: With 500 mentors and 1500 mentees, this will take 3 minutes to execute

# + id="cqta4tToYRIB"
for i in range(len(mentor_df)):

  # Convert mentor into skill list

    mentor_skill_list = mentor_df_skills_only.loc[i].values.tolist()

  # Create mentee df copy to conduct similarity tests

    mentee_df_copy = mentee_df.copy()

  # Add 'euc_dist' column

    mentee_df_copy['euc_dist'] = ''

  # Compute euclidean distance between the current mentor and each mentee

    for j in range(len(mentee_df)):

        mentee_skill_list = mentee_df_skills_only.loc[j].values.tolist()
        mentee_df_copy.at[j, 'euc_dist'] = \
            euclidian_distance(mentor_skill_list, mentee_skill_list)

  # Check if mentor can help mentee with career preparation
  # If not, filter down to only mentees who request technical help

    if not mentor_df.at[i, 'Career Preparation']:
        mentee_df_copy = mentee_df_copy[mentee_df_copy['Technical']
                == 1]

  # Filter mentees by time zone to match the mentor's time zone
  # Not necessary, but helpful once the data grows larger

    mentor_time_zone = mentor_df.at[i, 'time_zone'][0]
    mentee_df_copy = mentee_df_copy[mentee_df_copy[mentor_time_zone]
                                    == 1]

    top_five = mentee_df_copy.sort_values(by=['euc_dist']).head(5)

    profile_id_list = list(top_five['profile_id'])
    full_name_list = list(top_five['full_name'])

    mentee_suggestions = list(zip(profile_id_list, full_name_list))

    mentor_df.at[i, 'mentee_rec_1'] = mentee_suggestions[0]
    mentor_df.at[i, 'mentee_rec_2'] = mentee_suggestions[1]
    mentor_df.at[i, 'mentee_rec_3'] = mentee_suggestions[2]
    mentor_df.at[i, 'mentee_rec_4'] = mentee_suggestions[3]
    mentor_df.at[i, 'mentee_rec_5'] = mentee_suggestions[4]


# + [markdown] id="dWmejC20gR_8"
# # Condense Mentor dataframe back down to its original parameters + Mentee recommendations

# + id="6xW8bclTgaI-" colab={"base_uri": "https://localhost:8080/", "height": 309} outputId="7af84221-a866-48e3-a68f-8e760a478140"
mentor_df = mentor_df[[
    'profile_id',
    'skills',
    'career_capable',
    'skill_rank',
    'time_zone',
    'mentee_rec_1',
    'mentee_rec_2',
    'mentee_rec_3',
    'mentee_rec_4',
    'mentee_rec_5',
    ]]

mentor_df.head(3)

# + [markdown] id="gnoI_-5MhBtM"
# # Performance Testing
# ### Is the algorithm working?

# + colab={"base_uri": "https://localhost:8080/"} id="llAfrmRkYJzE" outputId="df1821c8-c239-4623-f9c7-f3be75d5aeec"
first_mentor_skills = mentor_df['skills'].head(1)
first_mentor_skills

# + [markdown] id="YH8_zH0TlOaU"
# ### View mentee recommendations for first mentor

# + colab={"base_uri": "https://localhost:8080/", "height": 81} id="vqii_ALhhtCx" outputId="d66338e6-35d7-489e-955b-2aa44a25f708"
mentor_df[['mentee_rec_1', 'mentee_rec_2', 'mentee_rec_3',
          'mentee_rec_4', 'mentee_rec_5']].head(1)

# + id="PwUxcSuiikq6"
# Get each mentee's profile id

mentee_rec_1_profile_id = mentor_df.loc[0, 'mentee_rec_1'][0]
mentee_rec_2_profile_id = mentor_df.loc[0, 'mentee_rec_2'][0]
mentee_rec_3_profile_id = mentor_df.loc[0, 'mentee_rec_3'][0]
mentee_rec_4_profile_id = mentor_df.loc[0, 'mentee_rec_4'][0]
mentee_rec_5_profile_id = mentor_df.loc[0, 'mentee_rec_5'][0]

# + [markdown] id="sG3gzdSBiVc3"
# ## Now let's look at each suggested mentee and their desired skills

# + id="MU6KcOLxiG1o"
mentee_1_df = mentee_df[mentee_df['profile_id']
                        == mentee_rec_1_profile_id]
mentee_2_df = mentee_df[mentee_df['profile_id']
                        == mentee_rec_2_profile_id]
mentee_3_df = mentee_df[mentee_df['profile_id']
                        == mentee_rec_3_profile_id]
mentee_4_df = mentee_df[mentee_df['profile_id']
                        == mentee_rec_4_profile_id]
mentee_5_df = mentee_df[mentee_df['profile_id']
                        == mentee_rec_5_profile_id]

# + colab={"base_uri": "https://localhost:8080/", "height": 206} id="ERLRb6vXmaa4" outputId="9dca6213-ae2c-4ef2-929b-bcb7e6cda4e8"
# Combine mentees into 1 dataframe

m = [mentee_1_df, mentee_2_df, mentee_3_df, mentee_4_df, mentee_5_df]
mentee_recs = m[0]
for _ in m[1:]:
    mentee_recs = mentee_recs.append(_)

# Mentee Desired Skills

mentee_recs[['profile_id', 'full_name', 'desired_skills']]

# + colab={"base_uri": "https://localhost:8080/"} id="VDzbpnXKnYIy" outputId="f2d89d88-1796-4d7a-b20b-04f9ad523e63"
# Mentor skills

mentor_df['skills'].head(1)

# + [markdown] id="H8LzRmvdjjci"
# ## Results will vary but there should be at least 1 matching skill between each mentee and mentor.

# + [markdown] id="gPI61crH__3W"
# ---

# + [markdown] id="kSSV9DcP_95l"
# ---

# + [markdown] id="P1OJQ7dC_Zgg"
# ---
# # Notebook Additions 01-28-22: Demand Forecasting

# + [markdown] id="vBEhMPdPADjg"
# ### Objective: Create a model that can forecast popular Mentee 'desired skills' by observing the past and present trends. 
#
# This model could enable a more focused search when trying to attract new Mentors with relevant skillsets.

# + colab={"base_uri": "https://localhost:8080/", "height": 142} id="oXTgR1pk_7qr" outputId="e5ed2dbc-05ef-4a56-aee2-5b0ed84359aa"
mentee_df = mentee_df[[
    'profile_id',
    'tech_or_career',
    'experience',
    'first_name',
    'last_name',
    'full_name',
    'time_zone',
    'email',
    'incarcerated',
    'list_convictions',
    'desired_skills',
    ]]
mentee_df.head(1)

# + id="C262maAQPLQL"


# + [markdown] id="nsxt5FQ1Iv-i"
# ### Time Series Forecasting
#
# We can build individual forecasts for each 'desired_skill' based on previous data. First, we can group the data into monthly statistics. Then we can conduct univariate time series forecasting using each month as column 1 and the statistics as column 2. Finally, we repeat the forecast for each skill and aggregate the data back together.
#
# Example Forecast for Python:
#
#
# Col1 ----------------- Col2
#
# (Time) ------------ (Python)
#
# Month 1 ------- 17 Mentees Desire Python
#
# Month 2 ------- 22 Mentees Desire Python
#
# Month 3 ------- 19 Mentees Desire Python
#
# Month 4 ------- 26 Mentees Desire Python
#
# Month 5 ------- [Model Prediction, ex: 23]
#
#

# + id="fC_bdRYmO71h"
import datetime
import random


# Stole this function from Nigel's notebook, thank you Nigel ;)

def random_date(
    start_y,
    start_m,
    start_d,
    end_y,
    end_m,
    end_d,
    ):
    start_date = datetime.date(start_y, start_m, start_d)
    end_date = datetime.date(end_y, end_m, end_d)
    time_between_dates = end_date - start_date
    days_between_dates = time_between_dates.days
    random_number_of_days = random.randrange(days_between_dates)
    random_date = start_date \
        + datetime.timedelta(days=random_number_of_days)
    return random_date


# + id="qffc-iokVXzP"
# Create new dataframe for forecasting

mentee_df_forecasting = mentee_df.copy()

# + colab={"base_uri": "https://localhost:8080/", "height": 391} id="6Ik3PLZ-HWgf" outputId="9e5fb2a9-10ef-45dd-9848-516480b4fa8b"
# Populate random dates into mentee dataframe

for i in range(len(mentee_df_forecasting)):
    mentee_df_forecasting.loc[i, 'date_submitted'] = random_date(
        2020,
        1,
        1,
        2022,
        1,
        27,
        )

mentee_df_forecasting.head()

# + id="Y56KdB07Hgby"
# Create new columns for each skill

for skill in skills:
    mentee_df_forecasting[skill] = 0

# OHE skills

for i in range(len(mentee_df_forecasting)):
    for skill in skills:
        if skill in mentee_df_forecasting.at[i, 'desired_skills']:
            mentee_df_forecasting.at[i, skill] = 1

# + colab={"base_uri": "https://localhost:8080/", "height": 311} id="lSKHmkGyP-mp" outputId="d99b7a67-dd78-4dcd-cbf3-2d037eb637ab"
mentee_df_forecasting.head(3)

# + [markdown] id="JMdA4xRp7N3Y"
# ## Create empty dataframe to store the skill counts

# + colab={"base_uri": "https://localhost:8080/", "height": 50} id="aRyf3PBHQZX6" outputId="0d60a88a-ad79-4ce5-e893-9168725b210b"
skill_counts_df = pd.DataFrame(columns=[
    'HTML',
    'CSS',
    'JavaScript',
    'Python',
    'Ruby',
    'C++',
    'Axios',
    'React',
    'Node.JS',
    'C#',
    'Django',
    'MongoDB',
    'SQL',
    'PostgreSQL',
    'NoSQL',
    'PHP',
    'Angular',
    'Microsoft Azure',
    'IOS',
    'Android',
    ])
skill_counts_df

# + [markdown] id="zuYCHSHwQa-b"
# ## Sum mentee skill counts and group them into months

# + id="ts0bI61YRVhe"
year_list = [2020, 2021, 2022]
month_list = [
    1,
    2,
    3,
    4,
    5,
    6,
    7,
    8,
    9,
    10,
    11,
    12,
    ]

for year in year_list:
    for month in month_list:

    # Adjust the day value depending on the month

        day = 31
        if month in [4, 6, 9, 11]:
            day = 30
        if month == 2:
            day = 28
            if year % 4 == 0:
                day = 29

        filtered_mentees = \
            mentee_df_forecasting[(mentee_df_forecasting['date_submitted'
                                  ] >= datetime.date(year=year,
                                  month=month, day=1))
                                  & (mentee_df_forecasting['date_submitted'
                                  ] < datetime.date(year=year,
                                  month=month, day=day))]
        monthly_stats = []
        for skill in skills:
            monthly_stats.append(filtered_mentees[skill].sum())

        month = datetime.date(year=year, month=month, day=day)
        skill_counts_df.loc[month] = monthly_stats


# + [markdown] id="m8jdu4lH4e8M"
# ## Dataframe showing each month's 'desired_skill' metrics for incoming mentees
#
# - Each row represents one month of data
# - The index includes the last day of the month just so that it can remain in datetime format for future manipulation (ex: 2020-01-31 represents 2020-01-01 thru 2020-01-31)

# + colab={"base_uri": "https://localhost:8080/", "height": 833} id="quecU4BkSpAw" outputId="57335613-4188-42d7-c6ef-d61a676c20b8"
skill_counts_df = skill_counts_df[datetime.date(year=2020, month=1,
        day=1):datetime.date(year=2022, month=1, day=31)]
skill_counts_df

# + colab={"base_uri": "https://localhost:8080/", "height": 265} id="rQEFNpVZZNFT" outputId="3247ce4b-cd86-4b69-eddc-0a8cd382e2d8"
# Testing - Let's look at the number of mentees who desire to learn HTML each month

from matplotlib import pyplot
skill_counts_df['HTML'].plot();

# + [markdown] id="p38VhTSK4U-N"
# ## Import Facebook's Prophet library for forecasting

# + id="-ntb1-TeaZ5-"
from fbprophet import Prophet

predictions_df = pd.DataFrame(columns=[
    'HTML',
    'CSS',
    'JavaScript',
    'Python',
    'Ruby',
    'C++',
    'Axios',
    'React',
    'Node.JS',
    'C#',
    'Django',
    'MongoDB',
    'SQL',
    'PostgreSQL',
    'NoSQL',
    'PHP',
    'Angular',
    'Microsoft Azure',
    'IOS',
    'Android',
    ])

# + [markdown] id="i8HGISB2s4iB"
# # Run Prophet model to generate predictions for upcoming month
#
# ### May take 2-3 minutes to run

# + colab={"base_uri": "https://localhost:8080/"} id="ddUGNw0Nor8U" outputId="813d91e8-2946-45ee-efe4-4c4d213dd575"
for skill in skills:

  # Instantiate Prophet model

    model = Prophet()

  # Create dataframe with 2 columns - Prophet requires 'ds' and 'y' names

    new_df = skill_counts_df[[skill]]
    new_df = new_df.reset_index()
    new_df.columns = ['ds', 'y']

  # Fit model and make prediction for the following month

    model.fit(new_df)
    future = model.make_future_dataframe(periods=1, freq='D')  # 'D' gives best acc. even tho data is monthly
    forecast = model.predict(future)

  # Grab prediction and put into predictions dataframe

    prediction = forecast.tail(1)['yhat'].iloc[-1]
    prediction = max(0, prediction)
    predictions_df.at[0, skill] = prediction

# + [markdown] id="CoQ2Wc0F0bef"
# # Predicted Incoming Desired Skills For Mentees Next Month
#
# Numbers represent the predicted amount of new mentees that will want to learn each particular skill next month

# + colab={"base_uri": "https://localhost:8080/", "height": 125} id="83UnRTfUpEvA" outputId="d13d7a94-e2e5-4d0d-9e3d-c885f131db6d"
predictions_df

# + [markdown] id="F4MpYDkc1Tuu"
# Prediction accuracy is difficult to judge at the moment since the skills that were populated into the original mentee dataframe were randomized and thus relatively uniform. 
#
# Example: Python popularity is approximately equal to Ruby which is approximately equal to C++ which is approximately equal to Axios. In the real world, there would be more variation.
#
# Not much of a pattern exists, so the model can't learn too much. Perhaps we can alter the randomization process in a future update in order to judge the prediction performance more clearly.

# + id="5N9wiWTAphIv"

