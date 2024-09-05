﻿ Hi everyone! 


﻿﻿The start.

My name is Pato (or Duck for English speakers, I guess). I've been playing Genshin Impact since day one, and this is the first time I’m trying to create something that could be useful for the community.

I started this project called Genshin Gacha Calculator (GGC) today, and it’s completely open to anyone with programming, math, or a combination of both skills to give me a hand.

The thing is, theoretically, this little script I made should be good to go, but I don't have practical proof yet. That’s where you, the reader and player, come in!


﻿﻿How it (almost) works

Using some mathematical concepts (I'm bad at math) and writing a script (I'm bad at programming), I’ve made a tool that can give you an approximate probability of pulling a 5-star item on a banner based on your current pity, official in-game probabilities, community calculations, and more.

The script allows you to use either just the official data or your personal account history to estimate your odds of getting a 5-star within a certain number of pulls.

This base probability calculation is done using the binomial distribution method (which I learned about just 7 days ago). It seems that a growing part of the community is testing this method, and the results are quite impressive. People have been able to predict 5-stars with less than 10 pulls of inaccuracy, which is better than nothing!

So, if you’re planning to pull for some powerful characters, it would be helpful if you could first try this little script to predict the results, and then leave a comment here sharing your experience.

This is just V.1.0, so it might have bugs, code errors, or formula mistakes. Please be patient, and if this works, we might have something really useful in our hands!


Updates.

    V.1.0:
    - Calculates the probability of getting a 5-star item in the number of pulls you specify, based on your current pity and official probabilities (for both character and weapon banners).
    - Allows you to input your wish history to make a personalized estimate (I recommend using Paimon.moe for the most accurate wish history).
    - For the personalized method, you need to provide the number of wishes you’ve made and the number of 5-stars you’ve pulled during those wishes.
    - The script takes into account soft pity and hard pity changes in 5-star pull chances for both character and weapon banners.


﻿﻿Future planning.

    - Add a feature to calculate the probability of pulling multiple 5-star items in a single ten-pull.
    - Add a feature to predict which of your upcoming ten-pulls has the highest chance of getting you a 5-star (though this is likely to be the first ten-pull after reaching soft pity).


﻿﻿Nerds: this is your moment.

As I mentioned, I’m not great at any of the skills required for this project. I main Itto, so maybe I’m not the right guy, but I’m already in!

If you find a way to optimize the code or improve the formula application for the current or future versions of the script, feel free to leave a comment or reach out to me on [Twitter](https://x.com/patontottv). You and your brain could be incredibly helpful for everyone!

We might be onto something here, so don’t miss out!
