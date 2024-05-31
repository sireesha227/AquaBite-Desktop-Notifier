"""
This file have all the list of words which are used for notifications.

It will return a randomly selected notifications or notification icons based on the function calls from
the main program.

"""
import random

breakfast = [
    "Good morning! ☀️ Your delicious breakfast is waiting to kick-start your day. Time to savor and shine!",
    "Rise and shine, breakfast explorer! Your morning feast is ready. Let the day begin with a tasty delight!",
    "Wake up to a breakfast fiesta! Your plate is set with love and nutrients. It's breakfast time, enjoy!",
    "Hello there! 🌅 Your breakfast masterpiece is calling. Embrace the flavors and make today amazing!",
    "A breakfast symphony is about to begin! Your morning melody of flavors awaits. Bon appétit!",
    "Morning magic awaits you! ✨ Your breakfast fairy has prepared something special. Time to indulge!",
    "Time to break the fast! Your morning masterpiece is ready to fuel your day. Enjoy every bite!",
    "Sun's up, breakfast's served! 🌞 Dive into the deliciousness waiting for you. It's the perfect start!",
    "Hey, breakfast buddy! Your morning spread is ready. Let's make today fantastic with a tasty beginning!",
    "Good vibes and great tastes coming your way! Your breakfast adventure is ready to unfold. Enjoy!",
    "Good morning, Sunshine! Your breakfast is served. Time to enjoy the first meal of the day, [Your Name]!",
    "Bonjour, [Your Name]! Your breakfast delight is ready. Let the flavors dance on your taste buds and energize your morning!",
    "Wakey-wakey, [Your Name]! Your morning spread is ready for you. Savor the goodness and kickstart your day!",
    "Hey [Your Name], rise and shine! Your breakfast adventure awaits. Dive in and make today delicious!",
    "Morning, [Your Name]! Your breakfast is like a warm hug for your taste buds. Embrace the flavors and conquer the day!",
    "Hello there, [Your Name]! Your breakfast bliss is calling. Time to treat yourself and start the day on a tasty note!",
    "Top of the morning to you, [Your Name]! Your breakfast symphony is about to begin. Enjoy every delicious note!",
    "Good day, [Your Name]! Your breakfast oasis is ready. Take a moment to savor the flavors and fuel your day!",
    "Greetings, breakfast enthusiast [Your Name]! Your morning ritual is set. Dive into your favorite flavors and make today amazing!",
    "Morning vibes, [Your Name]! Your breakfast is not just a meal; it's a celebration. Indulge and enjoy the deliciousness!",
    "Morning vibes, [Your Name]! 🌞 Top your morning yogurt with a handful of cherries🍒 and a drizzle of honey. It's a sweet way to kickstart your day!",
    "Hey, [Your Name]! 🎉 Create an avocado🥑 toast masterpiece with poached eggs 🍳 and a sprinkle of chili flakes. Add a side of sliced 🍅 tomatoes for extra freshness!",
    "Greetings! 🌼 Begin your day with a crunch. Slice up some apples🍎🍏 and pair them with almond butter for a tasty and energizing breakfast!",
    "Morning, [Your Name]! 🌞 Embrace the tropical vibes with a mango🥭 smoothie. Blend in some yogurt and top it off with a handful of juicy 🍍 pineapple chunks!",
    "Good day, [Your Name]! 🌺 Grab your favorite cereal 🥣, add a splash of milk, and toss in a mix of fresh 🍇 grapes. A crunchy breakfast awaits!",
    "Hey there! 🌻 Kickstart your day with a protein-packed breakfast. Scramble some eggs🍳 and pair them with avocado 🥑 and cherry 🍅 tomatoes. Delicious and nutritious!",
    "Hello, [Your Name]! 🌼 It's pancake o'clock! Whip up some fluffy pancakes 🥞 and top them with a handful of 🍌 banana slices. A sweet morning awaits!",
    "Rise and shine! 🌈 Start your day with a nutritious breakfast. How about some Greek yogurt with a sprinkle of granola and fresh 🍓 strawberries? Enjoy the flavors!"
]

lunch = [
    "Hello [Your Name]! It's lunchtime – the best part of the day. Your delicious meal is ready to make your taste buds dance!",
    "Lunch o'clock, [Your Name]! Your midday delight is calling. Take a break, savor the flavors, and recharge!",
    "Bonjour, [Your Name]! Your lunch rendezvous is here. Time to indulge in a plateful of goodness and enjoy a delightful break!",
    "Hey there, lunchtime hero [Your Name]! Your midday feast is served. Take a moment to savor and refuel for the afternoon!",
    "Good vibes served with lunch! [Your Name], your delicious midday escape is ready. Enjoy the flavors and take a well-deserved break!",
    "Hello, lunch enthusiast [Your Name]! Your midday pick-me-up is ready. Take a pause, relish the moment, and enjoy your tasty break!",
    "Lunchtime cheer, [Your Name]! Your delicious meal is set to brighten up your day. Bon appétit and enjoy your well-deserved break!",
    "Rise and dine, [Your Name]! Your lunch adventure awaits. Take a moment to savor the flavors and make your break delightful!",
    "Greetings, lunchtime explorer [Your Name]! Your midday escape is here. Dive into your tasty meal and enjoy a moment of deliciousness!",
    "Good day, [Your Name]! It's lunchtime, and your plate of joy is ready. Take a break, savor the moment, and recharge for the rest of the day!",
    "Time to refuel, [Your Name]! Your delicious lunch is ready to make your midday brighter. Take a moment to enjoy!",
    "Hey [Your Name], it's lunchtime! Your tasty break is calling. Treat yourself to a delightful meal and recharge for the afternoon!",
    "Lunch o'clock, [Your Name]! Your midday delight is served. Indulge in the flavors and take a break for yourself.",
    "Hello [Your Name], your lunch adventure begins now! Savor each bite and make your midday break a moment of joy.",
    "Bonjour, [Your Name]! Your lunch rendezvous is ready. Take a pause, relish the flavors, and enjoy a moment of deliciousness!",
    "Lunchtime joy, [Your Name]! Your plate of goodness is here. Take a break, savor the moment, and recharge for the rest of the day!",
    "Good vibes served with lunch! [Your Name], your midday escape is ready. Bon appétit and enjoy the flavors of your delightful meal!",
    "Rise and dine, [Your Name]! Your lunchtime delight awaits. Take a moment to savor the flavors and make your break delightful!",
    "Greetings, lunchtime connoisseur [Your Name]! Your midday feast is ready. Dive into your tasty meal and enjoy a moment of deliciousness!",
    "Good day, [Your Name]! Lunch is served, and it's time to treat yourself to a flavorful break. Enjoy every bite and recharge for the afternoon!",
    "Hey [Your Name]! 🌱 Time for a lunch adventure🥗. Whip up a colorful salad with crisp lettuce, cherry 🍅 tomatoes, crunchy cucumbers, and creamy 🧀 feta. Enjoy the freshness!",
    "Greetings! 🌼 Warm up your day with a hearty soup🍲. Try a veggie-packed minestrone with carrots, zucchini, 🌽 corn, and a handful of spinach. Delightful and nutritious!",
    "Hola [Your Name]! 🎉 It's 🌮taco o'clock. Load up your tortillas with grilled veggies, black beans, salsa, and a sprinkle of cilantro. Ole! 🌶️",
    "Good day! 🌞 Dive into a delightful eggplant🍆 dish. Roast or grill slices of eggplant, layer them with tomato 🍅 sauce and mozzarella 🧀 for a veggie-packed treat!",
    "Buongiorno, [Your Name]! Enjoy a pasta🍝 feast with a medley of sautéed veggies like bell peppers, cherry 🍅 tomatoes, and broccoli. Top it off with a drizzle of olive oil! 🌿",
    "Hi [Your Name]! 🌈 Boost your lunch with broccoli🥦 power. Steam or stir-fry broccoli florets and toss them with quinoa and a sprinkle of sesame seeds. Yum!",
    "Hello! 🌸 Pack your lunch 🍱bento-style. Include cucumber slices, snap peas, carrot sticks, and edamame for a colorful and crunchy lunchbox. Enjoy each bite!",
    "Hi! Create a veggie-filled noodle bowl🍜 with bok choy, bell peppers, and snow peas. Pour over some soy sauce for an Asian-inspired delight!"
]

dinner = [
    "🌙 Good evening, [Your Name]! Your delightful dinner is ready to turn your night into a feast. Enjoy the flavors and relax!",
    "Dinnertime alert! 🍽️ [Your Name], your evening delight is calling. Unwind and savor the goodness on your plate!",
    "Hey there, dinner hero! 🌟 Your evening masterpiece is served. Take a break, enjoy your meal, and let the relaxation begin!",
    "Time for a delicious dinner journey! 🚀 [Your Name], your nighttime feast is ready. Treat yourself and savor every bite!",
    "Evening bliss on a plate! 🌇 [Your Name], your dinner oasis is here. Take a moment, indulge, and enjoy the tranquility of the night.",
    "Dinner magic in the air! ✨ [Your Name], your evening delight is ready. Savor the flavors and let the relaxation set in.",
    "Dinner o'clock has arrived! ⏰ [Your Name], your plate of joy is waiting. Take a break, enjoy your meal, and unwind for the night.",
    "Good evening, dinner enthusiast! 🌆 Your nighttime feast is served. Indulge, relax, and enjoy the deliciousness on your plate!",
    "Greetings, dinner connoisseur! 🍲 [Your Name], your evening escape is ready. Dive into your tasty meal and unwind for the night.",
    "Nighttime flavors on the horizon! 🌌 [Your Name], your dinner delight is here. Take a moment, savor the meal, and enjoy the tranquility of the evening.",
    "🌟 Evening delight, [Your Name]! Your dinner masterpiece is ready. Time to unwind, savor, and enjoy the quiet moments.",
    "Dinner time, starlight! 🌙 [Your Name], your evening feast is served. Take a break, enjoy your meal, and relax into the night.",
    "Nightfall feast alert! 🍽️ [Your Name], your evening adventure in flavors is calling. Dive in and make it a memorable dinner!",
    "🌆 Twilight treat, [Your Name]! Your nighttime delight is ready to be savored. Indulge and let the evening magic unfold.",
    "Dinner magic in the air! 🌠 [Your Name], your plate of joy awaits. Take a pause, enjoy your meal, and let the night embrace you.",
    "Evening rendezvous with flavors! 🍲 [Your Name], your dinner escape is here. Relish the moment and enjoy a tranquil night.",
    "🌄 Sunset flavors, [Your Name]! Your dinner oasis is ready. Take a moment to savor, relax, and enjoy the evening serenity.",
    "Good evening, dining maestro! 🌃 [Your Name], your nighttime feast is served. Unwind, indulge, and let the flavors dance on your palate.",
    "Nighttime gourmet journey! 🌌 [Your Name], your dinner delight is calling. Enjoy every bite and embrace the calm of the evening.",
    "Starlit dinner vibes! ✨ [Your Name], your evening joy on a plate is ready. Savor the flavors and relax into a peaceful night."
]

snacks = [
    "🕒 Snack time alert! [Your Name], it's time for a delightful break. How about enjoying a refreshing 🍦 ice cream to sweeten your evening?",
    "Evening munchies calling! 🍪 [Your Name], your tasty snack awaits. Grab some crunchy 🥨 pretzels or indulge in a sweet treat like a 🍰 cupcake!",
    "Snack o'clock is here! ⏰ [Your Name], satisfy your cravings with a cool 🍨 frozen yogurt or a yummy piece of 🍫 chocolate. Enjoy your evening treat!",
    "Craving a delightful break? 🍬 [Your Name], how about a handful of your favorite 🍿 popcorn or a delicious 🧁 muffin for a perfect evening snack?",
    "Snack attack incoming! 🚀 [Your Name], it's time for a snack adventure. Grab a 🥤 refreshing drink and pair it with some tasty 🍩 donuts!",
    "Evening nibbles time! 🌙 [Your Name], unwind with a classic combo – a scoop of 🍨 ice cream and a slice of 🍰 cake. Treat yourself!",
    "Snack paradise awaits! 🍭 [Your Name], your favorite treats are ready. Choose between a fruity 🍉 popsicle or some crispy 🍟 fries. Enjoy!",
    "Snack sensation alert! 🎉 [Your Name], make your evening exciting with a delicious 🍦 sundae or a slice of your favorite 🍪 cookie. Indulge away!",
    "Snack magic in the air! ✨ [Your Name], elevate your evening with a cool 🍦 gelato or a scrumptious piece of 🍰 cheesecake. Enjoy the flavors!",
    "Evening snack vibes! 🌇 [Your Name], take a pause and treat yourself to a classic combo – a cone of 🍦 ice cream and a handful of 🥨 pretzels. Delightful!"
    "🌆 Snack time alert! [Your Name], it's time for a delicious evening treat. Grab your favorite snack and enjoy a delightful break!",
    "Evening munchies calling! 🍿 [Your Name], your tasty snack is ready to make your evening extra enjoyable. Treat yourself!",
    "Snack o'clock is here! ⏰ [Your Name], indulge in a tasty evening delight. What's your snack of choice today?",
    "Craving a delightful break? 🍪 [Your Name], your evening snack is ready to satisfy those cravings. Enjoy every bite!",
    "Snack attack incoming! 🚀 [Your Name], it's time to munch on something delicious. Grab a snack and make your evening awesome!",
    "Evening nibbles time! 🌙 [Your Name], your favorite snacks are waiting for you. Take a break and enjoy the deliciousness!",
    "Snack paradise awaits! 🍬 [Your Name], treat yourself to a delightful evening snack. Unwind and savor the flavors!",
    "Snack sensation alert! 🎉 [Your Name], it's time for a tasty break. Grab your favorite snack and make your evening more enjoyable!",
    "Snack magic in the air! ✨ [Your Name], your evening treat is ready. Indulge and enjoy the delicious moments!",
    "Evening snack vibes! 🌇 [Your Name], take a pause and enjoy a tasty snack to brighten up your evening. What's on your snack menu?"
]

water = [
    "Hydration Alert! Time to give your body a sip of love. Take a break and drink some water!",
    "Hey there! Your body is thirsty grab that water bottle and stay refreshed!",
    "Don't forget to hydrate! Your body is like a plant, and water is its sunshine. Take a moment to sip!",
    "Water break incoming! Your body is calling for hydration. Take a minute to sip and conquer!",
    "Cheers to H2O! It's time for a hydration break. Your body will thank you!",
    "Pause, hydrate, play! Your body needs water to keep the energy flowing. Take a sip break!",
    "Hydration mission activated! Take a moment to refresh yourself with a glass of water.",
    "Time for a water encore! Hydrate like it's your favorite routine. Go grab a glass!",
    "Hydrate, don't wait! Your body is asking for a water boost. Take a sip and power up!",
    "Water wizardry time! Cast a spell of hydration on yourself. Drink up and feel the magic!",
    "Hello [Your Name]! It's hydration o'clock - grab your water bottle and conquer the day!",
    "Time for a water break, [Your Name]! Your body is your biggest fan, and it's cheering for some hydration!",
    "Hey [Your Name], quick reminder from your body: it's thirsty Thursday! Take a sip and stay awesome.",
    "Good , [Your Name]! Your body is sending a gentle nudge - hydration time!",
    "Guess what, [Your Name]? It's the perfect moment for a water rendezvous. Hydrate and shine!",
    "Feeling a bit parched, [Your Name]? Your body is waving the hydration flag. Time to sip!",
    "Hey [Your Name], the hydration fairy just dropped by to remind you to drink water. Ready for a sip?",
    "Hydration vibes just for you, [Your Name]! Take a moment, grab your water, and stay refreshed.",
    "Listen up, [Your Name]! Your body's hydration alarm is buzzing. Time to answer the call and drink up!",
    "Hey [Your Name]! 🏃‍♂️ Time for a droplet dash! Grab your water and hydrate like you're in a hydration marathon! 🚿🥤",
    "Blast off, [Your Name]! 🚀 Fuel your day with hydration. Grab your water bottle and let's soar to new levels of freshness! 💦🌌",
    "Ahoy, [Your Name]! ⚓ Dive into an ocean of hydration. Your water bottle is your ship set sail for a well-hydrated day!🥤💙",
    "Greetings, [Your Name]! ✨ Sprinkle some hydration stardust on your day. Grab your water, take a sip, and let the magic flow! 🪄💫",
    "Aloha, [Your Name]! 🌴 Transport yourself to a tropical paradise with every sip. Grab your water and imagine the beach vibes! 🏖️💧",
    "Hey [Your Name]! 🌈 Take a break, grab your water, and let's keep the hydration vibes flowing. Your body will be so happy! 🥳🚰",
    "Rise and shine, [Your Name]! 🌞 Time to soar with hydration. Grab your water bottle and stay refreshed on this adventure called life! 🌊💙",
    "Hello, [Your Name]! 🔥 Ignite your day with hydration. Take a sip, fuel your energy, and let's make today amazing! 💧✨",
    "Aloha, [Your Name]! 🏝️ Let's bring the tropical vibes to your hydration routine. Grab your water and imagine sipping from a coconut under the sun! 🥥🌊",
    "Hey [Your Name]! 🌦️ Taste the hydration rainbow one sip at a time! Grab your water, add some color to your day, and stay hydrated! 🌈🚰",
    "A friendly reminder, [Your Name] your body needs some H2O love. Take a hydration pause!"
]

#Changes the names list as per your requirements
names = ["Siri","Sireesha","Queen","Princess","Beautiful","Champ","Cutie"]

icons_water = ["1.png" , "2.png" , "3.png" , "4.png" , "5.png"]

icons_food = ["f1.png" , "f2.png" , "f3.png" , "f4.png" , "f5.png"]

# It return any random notification from water list
def water_notifications():
    return random.choice(water)

# It return any random notification from breakfast list
def breakfast_notifications():
    return random.choice(breakfast)

# It return any random notification from lunch list
def lunch_notifications():
    return random.choice(lunch)

# It return any random notification from dinner list
def dinner_notifications():
    return random.choice(dinner)

# It return any random notification from snacks list
def snacks_notifications():
    return random.choice(snacks)

# It return any random notification from names list
def customized_names():
    return random.choice(names)

# It return any random image from icons_water list
def water_icons():
    return random.choice(icons_water)

# It return any random image from icons_food list
def food_icons():
    return random.choice(icons_food)
