

#For formating
long_empty_spaces="‎‎‏‏‎‏‏‎ ‎‏‏‎ ‎‏‏‎ ‎‏‏‎ ‎‏‏‎ ‎‏‏‎ ‎‏‏‎ ‎‏‏‎ ‎‏‏‎ ‎‏‏‎ ‎‏‏‎ ‎‏‏‎ ‎‏‏‎ ‎‏‏‎ ‎‏‏‎ ‎‏‏‎ ‎‏‏‎ ‎‏‏‎ ‎‏‏‎ ‎‏‏‎ ‎‏‏‎ ‎‏‏‎ ‎‏‏‎ ‎‏‏‎ ‎‎‎‏‏‎‎‏‏‎‏‏‎ ‎‏‏‎ ‎‏‏‎ ‎‏‏‎ ‎‏‏‎ ‎‏‏‎ ‎‏‏‎ ‎‏‏‎ ‎"
empty_spaces="‏‏‎ ‏‏‎ ‏‏‎ ‏‏‎ ‏‏‎ "
empty_space="‏‏‎ ‎"

#role that is regarded as op
op_roles=["Owner"]
op_id = ["852937032150155294","387221209047367680"]

#normal response when bots command used  Mainly for testing
response="OK Sir/Madam" #Disabled
disabled_msg = "Sorry this command is Now Disabled"
#Prefixes
bot_prefix = "b!"
coin_prefixs = ["bartercoin","bc"]
bank_prefixs = ["bank","bb"]
test_prefixs = ["test","t"]
general_prefixs = ["general","g"]
calculate_prefixs = ["calculate","calc"]
minecraft_prefixs = ["minecraft","mc"]

#EasterEggs
easterEggs = {"sushi":"Mermaid"}

###Decaration of constants###

#Calculator
operators=["+","-","*","/","^","%"]

#Time
one_day = 86400 #in Seconds
one_min = 60 #in seconds
one_hour = 3600 #in seconds
one_day = 86400 #in seconds
one_week = 604800 #in seconds
one_month = 2.628e+6 #in seconds
#one_day = 60 #for Testing

#general
ip = "BarterCraft.aternos.me"
reminderRunning = True

#Bank
bankRunning = True
bank_saveings_rate = 1/100
bank_invest_rate = 10/100
bank_min_saveings = 0
bank_min_invest = 10
bank_rates_title = "Rates"
bank_rates_desc = "Bank Info/Rates :bank:\nDaily Rates"
bank_rates = [{"name":"Savings",
              "value":f"Rate : {bank_saveings_rate}{empty_spaces}\nMinimum : {bank_min_saveings}{empty_spaces}"},
              {"name":"Invest",
              "value":f"Rate : {bank_invest_rate}{empty_spaces}\nMinimum : {bank_min_invest}{empty_spaces}"}]
  

#Coin
lb_default = 10
loginreward = 1
loginStreakBonus = 10/100

#Channels
taskChannelid=867438609333223465 #acutall
#taskChannelid=867442165663662111 #test server

###Commands###
t_cmds={"showdata":["showdata","show","s"],
        "showreminder":["showreminder","sr"]}

bb_cmds={"savings":["savings","s"],
         "invested":["invested","is"],
         "claim":["claim","c"],
         "withdraw":["withdraw","w"],
         "addsavings":["addsavings","save","as"],
         "invest":["invest","i"],
         "rates":["rates","rate","r"]}

bc_cmds={"balance":  ["balance","bal","b"],
      "setbalance":  ["setbalance","setbal","s"],
      "addbalance":  ["addbalance","addbal","a"],
      "transfer":    ["transfer","pay","send","give","p"],
      "create":      ["create","start","make","c"],
      "leaderboard": ["leaderboard","lb","balancetop","baltop","bt"],
      "delete":      ["delete","leave","stop","d"],
      "deleteall":   ["deleteall","dall"],
      "daily":       ["daily","dailyclaim","dc","claimdaily","cd"],
      "update":      ["update","u"],
      "reminddaily": ["reminddaily","rd","dailyreminder","reminder","dr","r"],
      "updatename":  ["updatename","updaten","un","uname"],
      "getdaychange":["getdaychange","daychange","dc","getdc","gdc"]}

g_cmds={"help":      ["help","h"],
        "helpdetail":["helpdetail","hd"],
        "remindme":  ["remindme","rme"],
        "removereminder":["removereminder","rr"],
        "flipacoin":     ["flipacoin","coinflip","flipcoin","fc"]}

help_cmds={"bartercoin":  ["bartercoin","bc"],
           "barterbank":  ["barterbank","bcb","bank","bb"],
           "calculator":  ["calculator","calc"],
           "general":     ["general","g"],
           "minecraft":   ["minecraft","mc"]}

mc_cmds={"whitelist": ["whitelist","w"],
         "ip":        ["ip","IP"]
}


db_format = {
    "ID": "",
    "Name": "",
    "Discriminator": "",
    "Balance": 0,
    "Banked": 0,
    "Invested": 0,
    "Investend":0,
    "Lastclaimed": 0,
    "Loginstreak": 0,
    "Dailyreminder":0}
    
time_format = {"seconds":["seconds","second","sec","s","secs"],
              "minutes": ["minutes","minute","min","m","mins"],
              "hours":   ["hours","hour","hr","h","hrs"],
              "days":    ["days","day","d"],
              "weeks":   ["weeks","week","w"],
              "months":  ["months","month","mo"],
              "years":   ["years","year","y"]}

###Messages###

#Special Messages
underWork_msg = "It is Currently Under Work. Please use this later"
hiddenFound_msg = "Your not Supposed to do that"
noChannel_msg = "Sorry the channel does not exist. Msg Staff for fixing this!!"
improperData_msg = "Please enter the data correctly"
uDontHaveAcc = "Sorry you dont have an Account"
nameDontHaveAcc = " dont have an Account."
accDoesNotExist = "Sorry the account does not exists"
couldNotGetDB = "Sorry Could not get data from database. Please Try again"
forgotMention = "Sorry you forgot to mention the user"
errorOccured = "Sorry an error occured, Error:"
unknownError = "Sorry something didnt work as intended"

##General##

reminderSet = "Reminder has been set, We will remind you"
notReminderSet = "Could not set reminder"
reminderRemoved = "Reminder has been removed, We wont remind you"
notReminderRemoved = "Could not remove reminder"

#Whitelist request        wl means Whitelist
wl_noServerSent_msg = "Did not send server"
wl_requestSent_msg = "Whitelist Request Sent"


##BarterCOin##
coinRunning = True
couldNotAddMoney = "Sorry, Could not add money to the account"
couldNotSetMoney = "Sorry, Could not set money to the account"
invalidAmount = "Sorry, Invalid amount"
accAlreadtCreatedFor = "Sorry Account is already Created for "
accCreatedFor = "Account Created for "
updateSuccess = "Successfully updated database"
dailyReminder_msg = "Reminder to Claim your daily reward"
infoUpdateSuccess = "Successfully updated the Name and Discriminator"
infoUpdateFail = "Failed to updated Name and Discriminator"
couldNotDelete = "Unable to delete the account"

###Help###
#Calculator Help     calch means CalculatorHelp
calch_title = "Calculator"
calch_desc = "Calculator commands :abacus:"
calch = [ {"name":"Addition",
        "value":f"""Command:
        {bot_prefix}{calculate_prefixs[1]} 10+999.412{empty_spaces}
        {empty_space}"""},

        {"name":"Subtraction",
        "value":f"""Command:
        {bot_prefix}{calculate_prefixs[1]} 92-360{empty_spaces}
        {empty_space}"""},

        {"name":"Multiplication",
        "value":f"""Command:
        {bot_prefix}{calculate_prefixs[1]} 101*20{empty_spaces}
        {empty_space}"""},

        {"name":"Division",
        "value":f"""Command:
        {bot_prefix}{calculate_prefixs[1]} 360/420{empty_spaces}
        {empty_space}"""},

        {"name":"Square",
        "value":f"""Command:
        {bot_prefix}{calculate_prefixs[1]} 8^4{empty_spaces}
        {empty_space}"""},

        {"name":"Modulo",
        "value":f"""Command:
        {bot_prefix}{calculate_prefixs[1]} 360%11{empty_spaces}
        {empty_space}"""}
       ]

#BarterCoin Help     bch means Bartercoinhelp
bch_title = "BarterCoin"
bch_desc = "BarterCoin commands :coin:"
bch = [ {"name":"Create account",
        "value":f"""Command:{empty_spaces}
        {bot_prefix}{coin_prefixs[0]} {bc_cmds['create'][0]}{empty_spaces}
        {empty_space}"""},

        {"name":"Transfer money",
        "value":f"""Command:{empty_spaces}\n{bot_prefix}{coin_prefixs[0]} {bc_cmds['transfer'][0]} (amount) (user){empty_spaces}
        {empty_space}"""},

        {"name":"Claim daily",
        "value":f"""Command:{empty_spaces}
        {bot_prefix}{coin_prefixs[0]} {bc_cmds['daily'][0]}{empty_spaces}
        {empty_space}"""},

        {"name":"Check balance",
        "value":f"""Command:{empty_spaces}
        {bot_prefix}{coin_prefixs[0]} {bc_cmds['balance'][0]}{empty_spaces}
        {empty_space}"""},

        {"name":"View leaderboard",
        "value":f"""Command:{empty_spaces}
        {bot_prefix}{coin_prefixs[0]} {bc_cmds['leaderboard'][0]} [How many to list]{empty_spaces}
        {empty_space}"""},

        {"name":"Delete account",
        "value":f"""Command:{empty_spaces}
        {bot_prefix}{coin_prefixs[0]} {bc_cmds['delete']}{empty_spaces}
        {empty_space}"""},

        {"name":"Add Daily Reminder",
        "value":f"""Command:{empty_spaces}
        {bot_prefix}{coin_prefixs[0]} {bc_cmds['reminddaily'][0]} True{empty_spaces}
        {empty_space}"""},
        
        {"name":"Remove Daily Reminder",
        "value":f"""Command:{empty_spaces}
        {bot_prefix}{coin_prefixs[0]} {bc_cmds['reminddaily'][0]} False{empty_spaces}
        {empty_space}"""},

        {"name":"Update Name/Discriminator",
        "value":f"""Command:{empty_spaces}
        {bot_prefix}{coin_prefixs[0]} {bc_cmds['updatename'][0]}{empty_spaces}
        {empty_space}"""}
       ]

#BarterBank Help     bbh means BarterBankHelp
bbh_title = "Bank"
bbh_desc = "Bank commands :bank:"
bbh = [ {"name":"Add Savings",
        "value":f"""Command:{empty_spaces}
        {bot_prefix}{bank_prefixs[0]} {bb_cmds['addsavings'][0]} (amount){empty_spaces}
        {empty_space}"""},

        {"name":"Withdraw Savings",
        "value":f"""Command:{empty_spaces}
        {bot_prefix}{bank_prefixs[0]} {bb_cmds['withdraw'][0]} (amount){empty_spaces}
        {empty_space}"""},

        {"name":"View Savings",
        "value":f"""Command:{empty_spaces}
        {bot_prefix}{bank_prefixs[0]} {bb_cmds['savings'][0]}{empty_spaces}
        {empty_space}"""},

        {"name":"View Invested",
        "value":f"""Command:{empty_spaces}
        {bot_prefix}{bank_prefixs[0]} {bb_cmds['invested'][0]}{empty_spaces}
        {empty_space}"""},

        {"name":"Invest Money",
        "value":f"""Command:{empty_spaces}
        {bot_prefix}{bank_prefixs[0]} {bb_cmds['invest'][0]} (amount) (Time to invest) (Unit of Time){empty_spaces}
        {empty_space}"""},

        {"name":"Claim Invested",
        "value":f"""Command:{empty_spaces}
        {bot_prefix}{bank_prefixs[0]} {bb_cmds['claim'][0]}{empty_spaces}
        {empty_space}"""},

        {"name":"View Rates",
        "value":f"""Command:{empty_spaces}
        {bot_prefix}{bank_prefixs[0]} {bb_cmds['rates'][0]}{empty_spaces}
        {empty_space}"""}
        
       ]


#Minecraft Help mch means minecraftHelp
mch_title = "Minecraft"
mch_desc = "Minecraft commands"
mch = [{"name":"Whitelist",
        "value":f"""Command:{empty_spaces}
        {bot_prefix}{minecraft_prefixs[0]} {mc_cmds['whitelist'][0]} (Username) [Server]{empty_spaces}
        {empty_space}"""},

        {"name":"IP",
        "value":f"""Command:{empty_spaces}
        {bot_prefix}{minecraft_prefixs[0]} {mc_cmds['ip'][0]}{empty_spaces}
        {empty_space}"""}
]

#General Help     gh means generalHelp
gh_title = "General"
gh_desc = "General commands :thought_balloon:"
gh = [ {"name":"Help",
        "value":f"""Command:{empty_spaces}
        {bot_prefix}{g_cmds['help'][0]}{empty_spaces}
        {empty_space}"""},

        {"name":"Help Detail",
        "value":f"""Command:{empty_spaces}
        {bot_prefix}{g_cmds['helpdetail'][0]}{empty_spaces}
        {empty_space}"""},

        {"name":"Add Reminder",
        "value":f"""Command:{empty_spaces}
        {bot_prefix}{g_cmds['remindme'][0]} (time) (unit) (reason){empty_spaces}
        {empty_space}"""},

        {"name":"Remove Reminder",
        "value":f"""Command:{empty_spaces}
        {bot_prefix}{g_cmds['removereminder'][0]}{empty_spaces}
        {empty_space}"""},

        {"name":"Flip A Coin",
        "value":f"""Command:{empty_spaces}
        {bot_prefix}{g_cmds['flipacoin'][0]}{empty_spaces}
        {empty_space}"""}
       ]

#Help Menu  hm means helpMenu
hm_title = "Help Menu"
hm_desc = "Help commands"
hm = [ {"name":"General :thought_balloon:",
        "value":f"""Command:{empty_spaces}
        {bot_prefix}{g_cmds['help'][0]} {general_prefixs[0]}{empty_spaces}
        {empty_space}"""},

        {"name":"BarterCoin :coin:",
        "value":f"""Command:{empty_spaces}
        {bot_prefix}{g_cmds['help'][0]} {coin_prefixs[0]}{empty_spaces}
        {empty_space}"""},

        {"name":"Bank :bank:",
        "value":f"""Command:{empty_spaces}
        {bot_prefix}{g_cmds['help'][0]} {bank_prefixs[0]}{empty_spaces}
        {empty_space}"""},

        {"name":"Calculator :abacus:",
        "value":f"""Command:{empty_spaces}
        {bot_prefix}{g_cmds['help'][0]} {calculate_prefixs[1]}{empty_spaces}
        {empty_space}"""},

        {"name":"Minecraft",
        "value":f"""Command:{empty_spaces}
        {bot_prefix}{g_cmds['help'][0]} {minecraft_prefixs[1]}{empty_spaces}
        {empty_space}"""}
       ]



##Help Detail##
#Calculator Help Detail     calchd means CalculatorHelpDetail
calchd_title = "Help Calculator :abacus:"
calchd_desc = f"Calculator, just a simple yet usefull tool with this bot you can do simple numbers operations like +,-,*,/,%,^. This still needs more features to make it usefull so with be updated in future.\n{empty_space}"
calchd = [ {"name":"How to use Calculator?",
        "value":f"""You need to use \"{calculate_prefixs[1]}\" as the prefix. Commands need to be sent in a channel where the bot and view and send messages.
        Example:
        {bot_prefix}{calculate_prefixs[1]} 1000*40 
        
        This command multiplies 1000 and 40 and give the result. It can accept only float values.
        {empty_space}"""}
       ]

#BarterCoin Help Detail    bchd means BartercoinHelpDetail
bchd_title = "Help BarterCoin :coin:"
bchd_desc = f"BarterCoin or BC is a coin and this bot handles the coin you can use this coin like a real coin, you can transfer it to other users.\n{empty_space}"
bchd = [ {"name":"How to use Bartercoin Commands?",
        "value":f"""You need to use \"{bot_prefix}{coin_prefixs[0]}\" as the prefix. Commands need to be sent in a channel where the bot and view and send messages.
        
        Aliases:
        {bot_prefix}{coin_prefixs}
        
        Example:
        {bot_prefix}{coin_prefixs[0]} {bc_cmds['create'][0]}
        This command creates an account for you to have BarterCoin.
        {empty_space}"""},

        {"name":"How to create an account?",
        "value":f"""You need to type \"{bot_prefix}{coin_prefixs[0]} {bc_cmds['create'][0]}\"
        When you create your account it will send a success message else it will send an error message.
        
        Aliases:
        {bot_prefix}{coin_prefixs} {bc_cmds['create']}
        
        Example:
        {bot_prefix}{coin_prefixs[0]} {bc_cmds['create'][0]}
        This command creates an account for you to have BarterCoin.
        {empty_space}"""},

        {"name":"How to transfer BarterCoin?",
        "value":f"""You need to type \"{bot_prefix}{coin_prefixs[0]} {bc_cmds['transfer'][0]} (amount) (ping the user to transfer to)\"
        
        Aliases:
        {bot_prefix}{coin_prefixs} {bc_cmds['transfer']}]
        
        Example: \n{bot_prefix}{coin_prefixs[0]} {bc_cmds['transfer'][0]} 10 @Scatter Playz
        This command transfers 10 Barter coin to user @Scatter Playz from the command users account.
        {empty_space}"""},

        {"name":"How to check your balance?",
        "value":f"""You need to type \"{bot_prefix}{coin_prefixs[0]} {bc_cmds['balance'][0]} \"
        
        Aliases:
        {bot_prefix}{coin_prefixs} {bc_cmds['balance']}
        
        Example:
        {bot_prefix}{coin_prefixs[0]} {bc_cmds['balance'][0]}
        This command shows your balance.
        {empty_space}"""},

        {"name":"How to view the leaderboard?",
        "value":f"""You need to type \"{bot_prefix}{coin_prefixs[0]} {bc_cmds['leaderboard'][0]} (how many to list. If none defaults to {lb_default}) \"
        
        Aliases:
        {bot_prefix}{coin_prefixs} {bc_cmds['leaderboard']}
        
        Example:
        {bot_prefix}{coin_prefixs[0]} {bc_cmds['leaderboard'][0]}
        This command shows the leaderboard.
        {empty_space}"""},

        {"name":"How to delete my account?",
        "value":f"""You need to type \"{bot_prefix}{coin_prefixs[0]} {bc_cmds['delete'][0]} \"
        
        Aliases:
        {bot_prefix}{coin_prefixs} {bc_cmds['delete']}
        
        Example:
        {bot_prefix}{coin_prefixs[0]} {bc_cmds['delete'][0]}
        This command deletes your account.\
        Seriously Don't use this command unless you want to. No refund will be provided if you lose BarterCoin by using this command.
        {empty_space}"""},

        {"name":"How to claim daily?",
        "value":f"""You need to type \"{bot_prefix}{coin_prefixs[0]} {bc_cmds['daily'][0]} \"
        
        Aliases:
        {bot_prefix}{coin_prefixs} {bc_cmds['daily']}
        
        Example:
        {bot_prefix}{coin_prefixs[0]} {bc_cmds['daily'][0]}
        This command claims you daily reward.
        {empty_space}"""},

        {"name":"How to enable Daily Claim Reminder?",
        "value":f"""You need to type \"{bot_prefix}{coin_prefixs[0]} {bc_cmds['reminddaily'][0]} True \"

        Aliases:
        {bot_prefix}{coin_prefixs} {bc_cmds['reminddaily']}

        Example:
        {bot_prefix}{coin_prefixs[0]} {bc_cmds['daily'][0]} True
        This command claims you daily reward.
        {empty_space}"""},

        {"name":"How to disable Daily Claim Reminder?",
        "value":f"""You need to type \"{bot_prefix}{coin_prefixs[0]} {bc_cmds['reminddaily'][0]} False \" 
        
        Aliases:
        {bot_prefix}{coin_prefixs} {bc_cmds['reminddaily']}
        
        Example:
        {bot_prefix}{coin_prefixs[0]} {bc_cmds['daily'][0]} False
        This command claims you daily reward.
        {empty_space}"""},

        {"name":"How to update Name/Discriminator",
        "value":f"""You need to type \"{bot_prefix}{coin_prefixs[0]} {bc_cmds['updatename'][0]} \" 
        
        Aliases:
        {bot_prefix}{coin_prefixs} {bc_cmds['updatename']}
        
        Example:
        {bot_prefix}{coin_prefixs[0]} {bc_cmds['updatename'][0]}
        This command updates your Name and Discriminator.
        {empty_space}"""}
       ]

#BarterBank Help Detail     bbhd means BarterBankHelpDetail
bbhd_title = "Help BarterBank :bank:"
bbhd_desc = f"BarterBank is where you can safely deposit Bartercoin and get interest or take loan.\n{empty_space}"
bbhd = [ {"name":"How to use BarterBank Commands?",
        "value":f"You need to use \"{bot_prefix}{bank_prefixs[0]}\" as the prefix. Commands need to be sent in a channel where the bot and view and send messages.."},

        {"name":"How to Add Savings?",
        "value":f"""Command:
        {bot_prefix}{bank_prefixs[0]} {bb_cmds['addsavings'][0]} (amount)

        Aliases:
        {bot_prefix}{bank_prefixs} {bb_cmds['addsavings']}

        Example:
        {bot_prefix}{bank_prefixs[0]} {bb_cmds['addsavings'][0]} 10
        This command add 10 to savings in bank from your account.
        {empty_space}"""},

        {"name":"How to Withdraw Savings?",
        "value":f"""Command:
        {bot_prefix}{bank_prefixs[0]} {bb_cmds['withdraw'][0]} (amount)

        Aliases:
        {bot_prefix}{bank_prefixs} {bb_cmds['withdraw']}

        Example:
        {bot_prefix}{bank_prefixs[0]} {bb_cmds['withdraw'][0]} 10
        This command withdraw 10 from your savings account to your account.
        {empty_space}"""},

        {"name":"How to View Savings?",
        "value":f"""Command:
        {bot_prefix}{bank_prefixs[0]} {bb_cmds['savings'][0]}

        Aliases:
        {bot_prefix}{bank_prefixs} {bb_cmds['savings']}

        Example:
        {bot_prefix}{bank_prefixs[0]} {bb_cmds['savings'][0]}
        This command shows you your savings.
        {empty_space}"""},

        {"name":"How to View Invested?",
        "value":f"""Command:
        {bot_prefix}{bank_prefixs[0]} {bb_cmds['invested'][0]}

        Aliases:
        {bot_prefix}{bank_prefixs} {bb_cmds['invested']}

        Example:
        {bot_prefix}{bank_prefixs[0]} {bb_cmds['invested'][0]}
        This command shows you your invested amount.
        {empty_space}"""},

        {"name":"How to Invest Money?",
        "value":f"""Command:
        {bot_prefix}{bank_prefixs[0]} {bb_cmds['invest'][0]} (amount) (Invest Time) (Unit of Time)

        Aliases:
        {bot_prefix}{bank_prefixs} {bb_cmds['invest']}

        Example:
        {bot_prefix}{bank_prefixs[0]} {bb_cmds['invest'][0]} 10 10 days
        This command invest 10 coin for 10 days.
        {empty_space}"""},

        {"name":"How to Claim Invested?",
        "value":f"""Command:
        {bot_prefix}{bank_prefixs[0]} {bb_cmds['claim'][0]}

        Aliases:
        {bot_prefix}{bank_prefixs} {bb_cmds['claim']}

        Example:
        {bot_prefix}{bank_prefixs[0]} {bb_cmds['claim'][0]}
        This command claims the amount invested.
        {empty_space}"""},

        {"name":"How to View Rates?",
        "value":f"""Command:
        {bot_prefix}{bank_prefixs[0]} {bb_cmds['rates'][0]}

        Aliases:
        {bot_prefix}{bank_prefixs} {bb_cmds['rates']}

        Example:
        {bot_prefix}{bank_prefixs[0]} {bb_cmds['rates'][0]}
        This command shows the rates of bank.
        {empty_space}"""}
       ]

#Minecraft Help Detail   mchd means MinecraftHelpDetail
mchd_title = "Help Minecraft"
mchd_desc = f"Here you can find commands related To Minecraft"
mchd = [{"name":"How to get whitelisted?",
        "value":f"""Command:
        {bot_prefix}{minecraft_prefixs[0]} {mc_cmds['whitelist'][0]} (username) [serverIP]
        
        Aliases:
        {bot_prefix}{minecraft_prefixs} {{mc_cmds['whitelist']}}
        
        Example:
        {bot_prefix}{minecraft_prefixs[0]} {mc_cmds['whitelist'][0]} Scatter_Playz
        This command send a message to the task channel for admins to see and manually Whitelist you.
        {empty_space}"""},

        {"name":"How to get the ip of the server",
        "value":f"""Command:
        {bot_prefix}{minecraft_prefixs[0]} {mc_cmds['ip'][0]}
        
        Aliases:
        {bot_prefix}{minecraft_prefixs} {{mc_cmds['ip']}}
        
        Example:
        {bot_prefix}{minecraft_prefixs[0]} {mc_cmds['ip'][0]}
        This command sends minecraft server ip
        {empty_space}"""}]

#General Help Detail     ghd means generalHelpDetail
ghd_title = "Help General"
ghd_desc = f"This only has help command for now but plan to add other mostly cosmetic commands.Will be worked on in furture\n{empty_space}"
ghd = [ {"name":"How to use help command?",
        "value":f"""Command:{empty_spaces}
        {bot_prefix}{g_cmds['help'][0]}{empty_spaces}
        
        Aliases:{empty_spaces}
        {bot_prefix}{g_cmds['help']}{empty_spaces}
        
        Example:{empty_spaces}
        {bot_prefix}{g_cmds['help'][0]}{empty_spaces}
        This command shows you the help menu.
        {empty_space}"""},

        {"name":"How to use help detail command?",
        "value":f"""Command:{empty_spaces}
        {bot_prefix}{g_cmds['helpdetail'][0]}{empty_spaces}
        
        Aliases:{empty_spaces}
        {bot_prefix}{g_cmds['helpdetail']}{empty_spaces}
        
        Example:{empty_spaces}
        {bot_prefix}{g_cmds['helpdetail'][0]}{empty_spaces}
        This command shows you the detail help menu.
        {empty_space}"""},

        {"name":"How to add reminder?",
        "value":f"""Command:{empty_spaces}
        {bot_prefix}{g_cmds['remindme'][0]} (time) (unit) (reason){empty_spaces}
        
        Aliases:{empty_spaces}
        {bot_prefix}{g_cmds['remindme']}{empty_spaces}
        
        Example:{empty_spaces}
        {bot_prefix}{g_cmds['remindme'][0]} 10 min remind me to poop{empty_spaces}
        This command add a reminder after 10 mins for remind me to poop.The bot will message u remind me to poop afer 10 mins
        {empty_space}"""},

        {"name":"How to remove reminder?",
        "value":f"""Command:{empty_spaces}
        {bot_prefix}{g_cmds['removereminder'][0]}{empty_spaces}
        
        Aliases:{empty_spaces}
        {bot_prefix}{g_cmds['removereminder']}{empty_spaces}
        
        Example:{empty_spaces}
        {bot_prefix}{g_cmds['removereminder'][0]}{empty_spaces}
        This command removes every reminder.
        {empty_space}"""}
        ,
        {"name":"How to flip a coin?",
        "value":f"""Command:{empty_spaces}
        {bot_prefix}{g_cmds['flipacoin'][0]}{empty_spaces}
        
        Aliases:{empty_spaces}
        {bot_prefix}{g_cmds['flipacoin']}{empty_spaces}
        
        Example:{empty_spaces}
        {bot_prefix}{g_cmds['flipacoin'][0]}{empty_spaces}
        This command flips a coin and return a Head or Tails.
        {empty_space}"""}
       ]

#Detail Help Menu  dhm means DetailHelpMenu
dhm_title = "Detail Help Menu"
dhm_desc = f"This is the menu for all the detail Help commands.\n{empty_space}"
dhm = [ {"name":"Help with General commands?",
        "value":f"""Command:
        {bot_prefix}{g_cmds['helpdetail'][0]} {general_prefixs[0]}
        This commands shows you how to use general commands.
        
        Aliases:
        {bot_prefix}{g_cmds['help']} {general_prefixs}
        {empty_space}"""},

        {"name":"Help with BarterCoin commands?",
        "value":f"""Command:
        {bot_prefix}{g_cmds['helpdetail'][0]} {coin_prefixs[0]}
        This commands shows you how to use BarterCoin commands.
        
        Aliases:
        {bot_prefix}{g_cmds['helpdetail']} {coin_prefixs}
        {empty_space}"""},

        {"name":"Help with BarterBank commands?",
        "value":f"""Command:
        {bot_prefix}{g_cmds['helpdetail'][0]} {bank_prefixs[0]}
        This commands shows you how to use BarterBank commands.
        
        Aliases:
        {bot_prefix}{g_cmds['helpdetail']} {bank_prefixs}
        {empty_space}"""},

        {"name":"Help with Calculator?",
        "value":f"""Command:
        {bot_prefix}{g_cmds['helpdetail'][0]} {calculate_prefixs[0]}
        This commands shows you how to use Calculator commands.
        
        Aliases:
        {bot_prefix}{g_cmds['helpdetail']} {calculate_prefixs}
        {empty_space}"""},

        {"name":"Help with Minecraft?",
        "value":f"""Command:
        {bot_prefix}{g_cmds['helpdetail'][0]} {minecraft_prefixs[0]}
        This commands shows you how to use Minecraft commands.
        
        Aliases:
        {bot_prefix}{g_cmds['helpdetail']} {minecraft_prefixs}
        {empty_space}"""}
       ]
