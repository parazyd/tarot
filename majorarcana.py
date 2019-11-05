# See LICENSE file for copyright and license details

# The Major Arcana
# Scraped from https://www.free-tarot-reading.net/free

majorarcana = [
    # {"Name":             ["Element", "Planet", "Zodiac"]},
    {"The Fool":           ["Air", "Uranus", None]},
    {"The Magician":       [None, "Mercury", None]},
    {"The High Priestess": [None, "Moon", None]},
    {"The Empress":        [None, "Venus", None]},
    {"The Emperor":        [None, None, "Aries"]},
    {"The Hierophant":     [None, None, "Taurus"]},
    {"The Lovers":         [None, None, "Gemini"]},
    {"The Chariot":        [None, None, "Cancer"]},
    {"Strength":           [None, None, "Leo"]},
    {"The Hermit":         [None, None, "Virgo"]},
    {"Wheel of Fortune":   [None, "Jupiter", None]},
    {"Justice":            [None, None, "Libra"]},
    {"The Hanged Man":     ["Water", "Neptune", None]},
    {"Death":              [None, None, "Scorpio"]},
    {"Temperance":         [None, None, "Saggitarius"]},
    {"The Devil":          [None, None, "Capricorn"]},
    {"The Tower":          [None, "Mars", None]},
    {"The Star":           [None, None, "Aquarius"]},
    {"The Moon":           [None, None, "Pisces"]},
    {"The Sun":            [None, "Sun", None]},
    {"Judgement":          ["Fire", "Pluto", None]},
    {"The World":          [None, "Saturn", None]},
]

majorarcana_readers = [
    "Aurora",
]

# {{{ majorarcana_card1
majorarcana_card1 = {
    "The Fool": {
        "Aurora": """You feel discontent or uneasy and feel a need for a change
                     in your life, a new direction, perhaps even an adventure.
                     You might not know where you want to go, just that you
                     don't want to stay where you are.

                     It's a time for optimism and major decisions - unexpected
                     influences could have a powerful effect on your
                     decision-making. Ask yourself, 'is what I desire really the
                     right thing for me'?""",
    },
    "The Magician": {
        "Aurora": """You feel a sense of purpose and the willpower to get things
                     done. Self-empowerment is the key word here. Any new
                     enterprises in love or career show great potential.

                     You feel that you have the ability to think on your feet
                     and, faced with opposition, the appearance of The Magician
                     is an excellent omen of success. Time to believe in
                     yourself and go for it!""",
    },
    "The High Priestess": {
        "Aurora": """You are very aware of the feminine power within, intuitive
                     and conscious at a spiritual level, looking for guidance
                     and answers, a secret to be revealed. You desire a wise
                     guide to help address your questions, and your intuition is
                     just that.

                     If you are male, the appearance of The High Priestess can
                     represent a woman who you care for very much and who truly
                     inspires you.""",
    },
    "The Empress": {
        "Aurora": """This is a time for nurturing, material and domestic comfort,
                     a feeling of abundance, harmony, joy and love.

                     A time for motherhood - you may already be pregnant or
                     thinking about motherhood, if female of course! If male,
                     this is a period of joy and abundance for you too - the
                     appearance of The Empress here could also indicate that
                     your mother or mother figure could be of great significance
                     or comfort at this time.

                     This is also a card of creativity so it is a good omen if
                     you are feeling creatively inspired at this time.""",
    },
    "The Emperor": {
        "Aurora": """You feel that success and achievement are on their way to
                     you. A man of significance will provide his support,
                     perhaps your father, husband/partner or boss - whoever it
                     is, he will give you steady support.

                     You feel confident and able to influence people and events,
                     as you have a great sense of your own authority. Expect
                     promotion at work or achieving greater status in life.

                     If you have been a victim of ill will, be assured that you
                     will win in the end.""",
    },
    "The Hierophant": {
        "Aurora": """You feel a need for advice or wise council or perhaps
                     spiritual consolation. Someone, or perhaps immediate
                     events, will provide moral and practical guidance. Perhaps
                     you are considering becoming such a tutor, counsellor or
                     spiritual advisor.

                     You desire the tried and tested traditional values, so when
                     considering your options, this approach will prove wiser
                     than adopting an unconventional novel approach. For
                     example, marriage is more likely to be your desire than a
                     living together situation.""",
    },
    "The Lovers": {
        "Aurora": """You want love or a new love in your life and a new
                     relationship is in the offering. Even if you are not
                     thinking about love, you're in for a surprise.

                     If faced with a choice it is an important one and could
                     affect the rest of your life.""",
    },
    "The Chariot": {
        "Aurora": """You feel everything is a constant battle at the moment, but
                     persevere and you will triumph in the end. Expect some good
                     news that will help you to keep going until you achieve
                     your goals.

                     This is a time of movement and change and of conflicts
                     ending in victory. You may well consider a journey that
                     relates to work or go for that new car you've been looking
                     at.""",
    },
    "Strength": {
        "Aurora": """You feel that despite the challenges you have been faced
                     with in the past, present or future, you will find the
                     strength and courage to succeed.

                     Whether you are recovering from ill health, a broken
                     marriage or relationship, or challenges at work, you will
                     find the willpower to come out on top.

                     If you are looking to give up any bad habits, such as
                     smoking or drinking for example, this is a good time to do
                     it.""",
    },
    "The Hermit": {
        "Aurora": """You may be feeling lonely at this time or going through a
                     period of introspection. If you are struggling to find
                     answers to your questions give it time, they will come.
                     This is a time for prudence and patience.

                     If you have been unwell this is a time for rest and
                     recuperation.""",
    },
    "Wheel of Fortune": {
        "Aurora": """Perhaps you feel due for a bit of good luck or indeed are
                     experiencing some at the moment.

                     The Wheel of Fortune is a card of destiny. What is
                     happening now we could call fate, so if positive things are
                     happening with your love life, career or finances this is
                     no coincidence.

                     If no such things are happening, expect a sudden change in
                     fortune!""",
    },
    "Justice": {
        "Aurora": """You are feeling that things will go your way. You believe
                     in fairness and justice in all things.

                     If you are considering partnership issues, personal or
                     professional, dealings will go well. Perhaps you are about
                     to sign a contract or legal document - this will be
                     beneficial to you.

                     If someone has done wrong to you it will be put right and
                     you will feel justice has been done.""",
    },
    "The Hanged Man": {
        "Aurora": """You feel a little confused and perhaps fearful because you
                     sense or know that there is someone or something you need
                     to give up to be able to move on. This self-sacrifice isn't
                     always clear - you may not even know quite what or whom you
                     should give up.

                     This is a time of passage from one phase of your life to
                     another and The Hanged Man can signify a time of spiritual
                     development too. Perhaps you need to try and look at things
                     from a different perspective.""",
    },
    "Death": {
        "Aurora": """Perhaps you feel that everything as you have known it is
                     falling apart. Unexpected changes and turmoil, end of a
                     job, end of a career, divorce or end of a relationship,
                     recovering from a bereavement or fear of bereavement.

                     Try not to worry too much: this time of absolute endings
                     heralds a brand new beginning, a period of great
                     transformation.""",
    },
    "Temperance": {
        "Aurora": """You feel a need for harmony and balance in your life and
                     indeed are starting to feel that some peace has already
                     been restored. If you have been through some tough times,
                     such as a breakup of a relationship or financial problems,
                     peace will be restored.

                     However if you are still experiencing problems, this is a
                     time for calm, careful control and patience and you will
                     soon have a sense of normality again.""",
    },
    "The Devil": {
        "Aurora": """You are feeling that the temptation of a certain
                     relationship, pastime or other form of pleasure is too hard
                     to resist - it's almost addictive. Question your motives,
                     these sorts of situations aren't generally good news.

                     You may also have rather low self-esteem at this time and
                     feel that there's not much hope for the future. Don't doubt
                     your abilities - try to be more positive. Think carefully,
                     you can still change direction.""",
    },
    "The Tower": {
        "Aurora": """You feel that the disruption and sweeping change you are
                     going through, or fear you are about to go through, will be
                     catastrophic. You need to recognise that such upheaval can
                     force new directions that you never dreamed possible.

                     Subconsciously you may have wanted change, but as is often
                     the case, the solution isn't always what we expect.

                     There could be more problems relating to your property, or
                     if considering a new property or move, progress will be
                     thwarted.""",
    },
    "The Star": {
        "Aurora": """You feel there is hope, or if you don't, have faith - a
                     tranquil period is imminent. If you have been ill, suffered
                     bereavement or disappointment in love, take heart, good
                     fortune is on its way. New horizons are indicated and you
                     will feel a new zest for life.

                     This is your wish card - if considering a new love affair,
                     new job or career, or travel, then go for it. You may also
                     receive a gift or gifts!""",
    },
    "The Moon": {
        "Aurora": """You feel confused, vulnerable and full of doubts. However,
                     all is not as it seems. Feel the fear and do it anyway,
                     because all will turn out well. Expect the new and
                     unexpected to show up and welcome it into your life.

                     Your turbulent emotions are muddying the waters so step
                     back and try to find clarity of mind, no matter how
                     difficult this proves to be. Things may seem tough or
                     confusing but stick with it, it's right for you. """,
    },
    "The Sun": {
        "Aurora": """You are feeling abundantly happy and joyful - if you don't,
                     be assured that you are about to enter a period of success
                     and fulfillment.

                     This is a time of pleasure, vitality and good health,
                     travel and holidays to be enjoyed. Good news around
                     children or the conception or birth of a longed-for baby.

                     The Sun heralds an ending to difficulties and a time to
                     celebrate with friends and loved ones.""",
    },
    "Judgement": {
        "Aurora": """You feel this is an end to an era or at least a certain
                     phase of your life - you are taking stock and looking where
                     you want to go from here.

                     The ending is not one for regret but for rejoicing. Soon
                     you will enjoy the rewards for your past efforts.

                     As with any period of endings, many opportunities will
                     present themselves and the choice that you make will have
                     far-reaching implications that could change your life
                     dramatically""",
    },
    "The World": {
        "Aurora": """You are about to reach, or are already enjoying, a period
                     of total fulfillment, wholeness and satisfaction - the
                     arrival of your heart's desires.

                     You feel satisfied with what you have achieved and are
                     enjoying the rewards for past efforts. A time of happy
                     outcomes, material wealth and greater spiritual
                     awareness.""",
    },
}
# }}}
# {{{ majorarcana_card2
majorarcana_card2 = {
    "The Fool": {
        "Aurora": """The Fool in this position suggests that what you most want
                     at this time is just to be happy, and you are searching for
                     one thing that will bring happiness.

                     You desire a new start but feel unsure of what you want or
                     where you want to go.

                     Romantically you may have mixed feelings about someone -
                     part of you wants to enter the relationship wholeheartedly,
                     part of you wants to hold back. So if you are in a
                     relationship that empowers you then stay - if not it is
                     time to move on.""",
    },
    "The Magician": {
        "Aurora": """What you most want is a new love in your life, and when
                     The Magician appears, a new love affair or perhaps a
                     rekindled affair is at hand.

                     All things new are possible, the result is up to you - it
                     depends on just how much you want it.""",
    },
    "The High Priestess": {
        "Aurora": """The cards suggest that what you most want at this time is
                     for a secret to be revealed - a secret held deep within
                     yourself or another.

                     Go within and listen to the still small voice of your heart
                     and instincts. The appearance of The High Priestess tells
                     you that the power of the divine feminine is with you -
                     trust it.""",
    },
    "The Empress": {
        "Aurora": """The cards suggest that at this time you desire comfort,
                     security and happiness and may well need some emotional
                     support and reassurance.

                     If you are considering having a baby the desire will be
                     very strong at this time, or perhaps you are already
                     pregnant and you have some concerns. If male, perhaps you
                     are considering fatherhood with someone but have concerns.

                     Things will turn out fine, just know that you are loved and
                     that there are people around you who care.""",
    },
    "The Emperor": {
        "Aurora": """The Emperor in this position suggests that what you most
                     want at this time is success and achievement, and the
                     support and influence of perhaps your father,
                     husband/partner or another man of significance in your life
                     who you believe could help.""",
    },
    "The Hierophant": {
        "Aurora": """Right now you want to have someone around you that you can
                     trust and confide in, knowing that they won't let you down.

                     There are moral issues here, knowing right from wrong, and
                     you may feel that you need some advice or wise counsel from
                     a teacher, priest, parent or someone you have a lot of
                     respect for, in order to help you make the right
                     decision.""",
    },
    "The Lovers": {
        "Aurora": """The cards suggest that what you most want at this time is to
                     know what choice to make - carry on as you are or take a
                     risk? The risk offers excitement and change and staying as
                     you are- well you know what that has to offer.

                     Dare to love, dare to live?""",
    },
    "The Chariot": {
        "Aurora": """The cards suggest that what you most want at this time is
                     success, to win and to never give up the fight.

                     You are successful and assertive in most things, or if you
                     haven't quite got the success you want, you will get it.

                     This is a time of movement and change - expect a journey
                     relating to work, or if you really want that car you've
                     been dreaming about, go get it!""",
    },
    "Strength": {
        "Aurora": """The cards suggest that what you most want at this time is
                     to find the strength and willpower to see you through and
                     achieve what you want.

                     It is important to come from a place of love and tolerance
                     though, not aggression. Put your fears to rest and develop
                     a positive attitude and you'll reap richer rewards.""",
    },
    "The Hermit": {
        "Aurora": """The Hermit here suggests that what you most want at this time
                     is to know what to do, as well as companionship or a lover
                     if you feel somewhat lonely or isolated at the moment.

                     Perhaps you are feeling exhausted and in need of a rest -
                     if you have been ill this is a time for rest and
                     recuperation.""",
    },
    "Wheel of Fortune": {
        "Aurora": """The Wheel suggests that you're looking for a turning point
                     in your life and positive change, and if that's the case
                     expect it now!

                     Life will go up a gear or two and events will accelerate
                     you forward. Destiny is at play here - have you noticed a
                     number of events that seem rather 'coincidental'? This is
                     synchronicity, trust it and go with the flow.""",

    },
    "Justice": {
        "Aurora": """The cards suggest that what you most want at this time is
                     for a fair and right outcome whether it concerns
                     relationships or business affairs. You feel that you are in
                     the right and that any decision or agreement to be made
                     should be in your favour.""",
    },
    "The Hanged Man": {
        "Aurora": """The cards suggest that what you most want at this time is
                     to have it all! Why should you have to give something or
                     someone up?

                     Perhaps you feel a victim and that events are not going as
                     planned. Trust that this is a passage from one phase of
                     your life to another.

                     If you are not sure what or who you need to give up, trust
                     that things will resolve themselves over time and whatever
                     the outcome it will ultimately be to your benefit.""",
    },
    "Death": {
        "Aurora": """The Death card suggests that what you most want at this
                     time is absolute change, to end what you no longer want and
                     start anew.

                     You may desire to transform your career or love life,
                     perhaps your whole lifestyle in general. However radical
                     such changes might be, embracing them will help you grow in
                     wisdom and experience.""",
    },
    "Temperance": {
        "Aurora": """The appearance of Temperance suggests you are craving some
                     peace and harmony, a sense of control and wish to feel that
                     life is flowing again. Perhaps you have been, or are
                     currently going through some tough times regarding a
                     relationship, financial worries or some other kind of loss.

                     Take heart that peace will be restored - this is a time for
                     you to be calm and patient and life will soon have a sense
                     of normality again.""",
    },
    "The Devil": {
        "Aurora": """The cards suggest that what you most want at this time you
                     can't have, and like the forbidden fruit this only makes it
                     all the more tempting. Alternatively you know you could go
                     for something, but it would be a bad choice and you'd be
                     doing it for all the wrong reasons.

                     Yes, you want passion and gratification - just be careful
                     where you go looking for it.""",
    },
    "The Tower": {
        "Aurora": """You're probably looking for an easy solution to a difficult
                     problem. However in life, turmoil and upheaval often bring
                     about positive change - just not quite as we would like it.

                     Seize this opportunity that is forcing change as a chance
                     for a new beginning.""",
    },
    "The Star": {
        "Aurora": """The Star suggests that what you most want at this time is
                     some good fortune, a bright and happy future.

                     If you have been ill, suffered bereavement or
                     disappointment in love, your luck is about to change. This
                     is your wish card - it will bring happiness, fulfillment
                     and good health. You may also receive a gift or gifts!""",
    },
    "The Moon": {
        "Aurora": """At this time you desire clarity and less of those confused
                     emotions that leave you fearful and vulnerable. You want to
                     know the outcome because you are so unsure about how you
                     feel.

                     Use your intuition to guide you away from deception and
                     ride this out - it will turn out alright in the end. The
                     Moon is also a good omen if you are in a clandestine
                     affair.""",
    },
    "The Sun": {
        "Aurora": """The Sun suggests that what you most want at this time is
                     some joy and pleasure in your life, perhaps a long-needed
                     holiday in the sun to re-charge your batteries.

                     You may have been through a period of challenges or a time
                     of limbo and inactivity. The Sun heralds an ending to
                     difficulties and a time to celebrate with friends and loved
                     ones, a time of pleasure and the possibility of good news
                     around children or the conception or birth of a longed-for
                     baby.""",
    },
    "Judgement": {
        "Aurora": """The cards suggest that what you most want at this time is
                     a new start - to close this chapter in your life and have a
                     brand new beginning.

                     This is not a time for regret but for rejoicing. Rewards
                     for past efforts will follow and you are sure to have many
                     opportunities presented to you. Life will pick up a pace
                     and the choices you make will have far-reaching
                     implications that could change your life dramatically. """,
    },
    "The World": {
        "Aurora": """You're most likely looking for a successful conclusion
                     after all your hard work and the arrival of The World in
                     your reading here suggests that's either happening now or
                     just around the corner.

                     This is a time for completion and satisfaction, the final
                     chapter is here and now - you've done your best and won
                     through.""",
    },
}
# }}}
# {{{ majorarcana_card3
majorarcana_card3 = {
    "The Fool": {
        "Aurora": """You are afraid of making the wrong decisions. There is a
                     warning here that foolhardy, impetuous actions could lead
                     to major problems.

                     Perhaps you feel that you don't have control over a
                     situation, either personal or professional. You may feel
                     unable to complete a task or stay in a current relationship
                     and fear the consequences of your decisions. Perhaps you
                     know deep down that what you want isn't really such a good
                     thing.""",
    },
    "The Magician": {
        "Aurora": """If there's a new man in your life you are probably asking
                     yourself if he can be trusted. Or perhaps this is a man of
                     influence in your life, a boss or adviser - take care in
                     whom you place your trust.

                     If you are feeling disappointed and your romantic desires
                     are unfulfilled at this time and you are wondering if they
                     ever will be, don't worry, this won't last.""",
    },
    "The High Priestess": {
        "Aurora": """You are feeling uneasy and insecure, something in your gut
                     is saying "be careful, all is not as it seems" - something
                     just doesn't feel right. Delay any decisions or actions
                     until you have answered your concerns.

                     If you are male this card could signify a significant woman
                     in your life being a bad influence right now.""",
    },
    "The Empress": {
        "Aurora": """You are feeling insecure, perhaps have money worries,
                     concerns over your children or maybe an unplanned
                     pregnancy. There are people around you who love and care
                     for you and they will give you support.

                    Try not to be overprotective and do not resort to emotional
                    blackmail, it won't do you any favors.""",
    },
    "The Emperor": {
        "Aurora": """You are sensing that success is just around the corner but
                     it feels elusive, just out of reach. You may be concerned
                     that the support and help you want from your father,
                     husband/partner or another man of significance in your life
                     won't materialise.

                     Trust and ask for the help you need, and success will be
                     yours.""",
    },
    "The Hierophant": {
        "Aurora": """Are you really your best counsel? Probably not at this
                     moment in time.

                     You are worried that you will sell yourself short and agree
                     to something that you don't feel morally comfortable with.
                     For example you may really desire marriage but the offer
                     has been 'let's live together'. You may be looking at a job
                     or business opportunity but you question how ethical it is.

                     Seek out an advisor you can trust such as a teacher,
                     priest, parent or anyone you have respect for. They will be
                     happy to help.""",
    },
    "The Lovers": {
        "Aurora": """Someone's heart is ruling their head! You are so afraid of
                     being hurt you are remaining paralyzed in non-action.

                     To have or not to have? To stay or to go? Throw caution to
                     the wind - great happiness awaits you if you can trust what
                     you feel and ignore the fear and do it anyway.""",
    },
    "The Chariot": {
        "Aurora": """The word failure isn't in your vocabulary. You are worried
                     things are more of a struggle than you expected, with more
                     delays and frustrations.

                     Things aren't going according to plan at all - just chill
                     out, calm that mind of yours and you'll find the strength
                     to battle on until you succeed. This is a period of
                     movement and change and conflicts ending in victory.""",
    },
    "Strength": {
        "Aurora": """You are fearful of lacking the willpower and strength to
                     deal with someone or something that concerns you.

                     Feeling negative and listening to all your fears will only
                     create failure and lost opportunities. Be as brave as a
                     lion but work compassionately and you'll be fine.""",
    },
    "The Hermit": {
        "Aurora": """You are worried about being on your own and afraid of
                     loneliness, and you simply don't know what to do. Take the
                     time to relax and eventually you will have the answers.

                     The Hermit signals a warning not to make hasty decisions,
                     so try not to get too stressed, and if you have been unwell
                     this is a time for rest and recuperation.""",
    },
    "Wheel of Fortune": {
        "Aurora": """You are in fear of everything taking a turn for the worst.
                     Perhaps you are experiencing a run of bad luck. You have to
                     trust that most of what we fear never happens and just as
                     The Wheel of Fortune turns downwards against you, it will
                     naturally turn upwards again and bring new good fortune
                     with it.

                     This difficult phase will pass.""",
    },
    "Justice": {
        "Aurora": """There could be agreements or legal affairs that concern you
                     and you certainly don't want to lose - you feel quite
                     strongly that you are in the right.

                     Stay calm and level-headed and seek sound counsel if you
                     need to.""",
    },
    "The Hanged Man": {
        "Aurora": """You fear letting go, yet this place of limbo and indecision
                     is not a good place to be.

                     Are you being emotionally blackmailed so you don't leave?
                     Don't be the victim.  Sometimes we have to have the
                     strength to let go to attract new positive possibilities
                     into our life.""",
    },
    "Death": {
        "Aurora": """You are afraid of experiencing turbulent and catastrophic
                     change, as we all are, yet such challenging transformation
                     in our lives helps create the space for something new.

                     If you are experiencing or have just experienced a job
                     loss, a bereavement, divorce or the end of a relationship,
                     these changes will allow new experiences and opportunities
                     to enter your life.""",
    },
    "Temperance": {
        "Aurora": """You are afraid that this period of harmony in your relationship
                     or life in general is not going to last.

                     Perhaps you fear that a rival is going to cause conflict
                     (or already has), threatening to upset the peace and
                     tranquility you are enjoying. Any quarrels will be
                     short-lived so just try and enjoy the moment for what it
                     is.

                     If life is not joyful and tranquil at the moment you may
                     fear that it never will be - take heart and be patient and
                     life will soon have a sense of normality again.""",
    },
    "The Devil": {
        "Aurora": """You are afraid that it's out of control. You simply cannot
                     resist this passionate attraction. Despite the fact it's
                     addictive and unlikely to be right, you just can't stop
                     yourself.

                     Whatever it is, a passion for someone who's not good for
                     you, money deals that are too good to be true or any other
                     kind of temptation, try to resist, as it is unlikely to
                     have a positive outcome.

                     If you're feeling low in self-belief and self-worth and
                     doubt your abilities - don't! Have confidence in yourself -
                     it's not too late to change direction.""",
    },
    "The Tower": {
        "Aurora": """You are afraid your world is falling apart: you're
                     experiencing sudden changes and disruption and you don't
                     know what to do.

                     Perhaps subconsciously you've wanted a solution to an issue
                     but didn't quite expect things to have turned out as they
                     have. Use this change as an opportunity for a new
                     beginning.""",
    },
    "The Star": {
        "Aurora": """You are fearful of the future and lacking in self-belief,
                     afraid your hopes will be dashed. Well don't be! This is
                     your wish card and signifies a time of joy and fulfilment.

                     Good health, possibly after a time of illness, and good
                     fortune will give you a new zest of life. If considering a
                     new love affair, new job or career, or travel, then go for
                     it. You may also receive a gift or gifts!""",
    },
    "The Moon": {
        "Aurora": """Lies and insecurity are likely to be prominent in your
                     life at the moment - you are afraid of being deceived and
                     feel that you are being misled. Trust your instincts and
                     let them guide you away from those who may seem charming
                     but are only out for their own gains.

                     Your turbulent emotions are muddying the waters - step back
                     and try to find clarity of mind, although this may seem
                     difficult. The Moon does help to illuminate the way and
                     don't worry, it will turn out alright in the end.""",
    },
    "The Sun": {
        "Aurora": """You are afraid that things seem too good to be true, so much
                     pleasure and joy - well enjoy it, sometimes we can be
                     pleasantly surprised!

                     If you have been unwell this is a time of rejuvenation and
                     good health. Perhaps you are afraid that things won't
                     actually get better - have faith you are about to enter a
                     happy and pleasurable time.

                     The Sun heralds an ending to difficulties and a time to
                     celebrate with friends and loved ones, a time of pleasure
                     and good news around children or the conception or birth of
                     a longed-for baby.""",
    },
    "Judgement": {
        "Aurora": """You are afraid that the conclusions you've been wanting are
                     delayed and fear any far-reaching changes ahead.

                     Perhaps things aren't turning out quite as you expected for
                     some reason - this is a period when your routine will be
                     changed dramatically.

                     Fear not, although events will seem to be moving at a real
                     pace, any choice you make will change life for the
                     better.""",
    },
    "The World": {
        "Aurora": """You are afraid of taking action and lack confidence and
                     willpower, but this is a time to be positive and proactive
                     to prevent loss of momentum, delays and stagnation.

                     Completion and success are only a step away. Don't give up,
                     lose heart or change direction when you are so close to the
                     finish line.""",
    },
}
# }}}
# {{{ majorarcana_card4
majorarcana_card4 = {
    "The Fool": {
        "Aurora": """This is an exciting time with lots of potential for fun
                     and wonderful experiences. Your confidence should be high,
                     it's a great time for new possibilities.

                     If you are considering leaving your job, home or
                     relationship, at some point you will.

                     An unexpected desire will be fulfilled, even before you
                     express it!""",
    },
    "The Magician": {
        "Aurora": """If considering any new enterprise or relationship you will
                     find the self-belief, confidence and ingenuity to make it a
                     success.

                     Perhaps you desire a promotion or pay increase at work

                     You may strongly and truly believe that if you were to
                     choose to work for yourself you could be prosperous.

                     Go for it!""",
    },
    "The High Priestess": {
        "Aurora": """All lines are open in your telephone exchange with your
                     intuition, and there is no better guide than this
                     intuition.

                     Listen.

                     Listen carefully and the secret you want revealed will be
                     shared with you.""",
    },
    "The Empress": {
        "Aurora": """The harvest is here; you are entering a cycle of
                     abundance, happiness and joy.

                     Creative energy is high so if you are considering starting
                     a family, a new job or artistic endeavour this is a
                     favourable time.

                     Relax and enjoy.""",
    },
    "The Emperor": {
        "Aurora": """You are self-assured and more than capable of influencing
                     people or events to achieve what you want.

                     What's more, support and guidance from your father,
                     husband/partner or another man of significance in your life
                     is there for the asking.

                     Make the most of your resources.""",
    },
    "The Hierophant": {
        "Aurora": """There is help at hand. Just ask for it.

                     If you are concerned about making the right decision there
                     is someone with the right moral fibre who can help.

                     You can receive Wise counsel and honest advice from a
                     teacher, priest or parent, or just someone you have a lot
                     of respect for. They are more than willing to help.""",
    },
    "The Lovers": {
        "Aurora": """New love and commitment will enter your life, even if
                     there's no one on the horizon - be prepared for a surprise.

                     Throw caution to the wind and expect joyous and happy times
                     ahead.""",
    },
    "The Chariot": {
        "Aurora": """Drive, drive, drive, that's what's going for you. You
                     certainly aren't a quitter.

                     The appearance of The Chariot tells of conflicts ending in
                     victory, so don't give up. Battle on and you will succeed.

                     This is a time of movement and change. Expect a journey
                     relating to work, and if you've had your eye on that car,
                     it will soon be yours.""",
    },
    "Strength": {
        "Aurora": """Brave heart!

                     Your self-confidence and courageous spirit is unstoppable
                     at the moment.

                     Be patient and compassionate, self-disciplined and strong
                     and you will reap great rewards for your courage.""",
    },
    "The Hermit": {
        "Aurora": """You are instinctively taking time to relax and reflect,
                     drawing on your inner strength and wisdom to guide you
                     through this difficult period in your life.

                     Time is a great healer, so even if you don't know quite
                     what to do now, you will eventually make the right
                     decision.

                     The Hermit signals a warning not to make hasty decisions.
                     Make sure you observe a period of rest and recuperation if
                     you have been unwell.""",
    },
    "Wheel of Fortune": {
        "Aurora": """Call it fate or destiny but the run of good luck or good
                     fortune you are experiencing or about to experience is
                     mostly not of your doing.

                     Enjoy this time.

                     If there seem to be a number of positive coincidences
                     happening in your life - this is known as synchronicity -
                     go with the flow and trust it.""",
    },
    "Justice": {
        "Aurora": """There is a karmic power to the Justice card, reward for
                     the good deeds you have done in the past.

                     This is a period of good luck even if you don't know why
                     you are being so favoured.

                     You will approach any issues concerning relationships or
                     business affairs with calm, balanced logic and any claim
                     will go in your favour.""",
    },
    "The Hanged Man": {
        "Aurora": """With patience this passive time, this time of feeling in
                     limbo and indecision, will pass and then you will know what
                     decisions to make, what or who to let go of and how to move
                     on.

                     Whatever self-sacrifice you have to make, you will feel a
                     better and stronger person for it.""",
    },
    "Death": {
        "Aurora": """A time of absolute endings and brand new beginnings, your
                     life is going through a period of great transformation.

                     Whilst change may be difficult, or even painful, you will
                     pull through.

                     You will be free for a brand new phase in your life.""",
    },
    "Temperance": {
        "Aurora": """You are about to enter a period of peace and harmony in
                     your relationship, career or life in general.

                     You will find a way of handling difficult circumstances
                     with calm confidence.

                     Life is flowing at this time - enjoy it.""",
    },
    "The Devil": {
        "Aurora": """There's a possibility of permanence here. If you're
                     considering a commitment in a relationship or marriage this
                     is a good sign.

                     However, question your motives because here we have
                     temptation and addiction, and a desire to be controlled or
                     controlling.

                     So use your intuition and if you recognise what you feel is
                     being sincere, great. If not you still have a chance to
                     change direction.

                     if considering giving up a bad habit, such as smoking or
                     drinking for example, now is a good time to start.""",
    },
    "The Tower": {
        "Aurora": """Sometimes sudden disruptive change is inevitable, and as
                     painful as it may seem, you come through it a stronger and
                     better person.

                     No matter how disruptive things are at the moment, or if
                     you feel life is really against you, reevaluate and move
                     on. Often a new direction can bring new opportunities you
                     never dreamed of.

                     If you have been planning to move home, you will be
                     experiencing setbacks.""",
    },
    "The Star": {
        "Aurora": """A wish come true, this is a time of good luck and fortune,
                     perhaps after a period of struggle and heartache.

                     Good health, possibly after a time of illness, and good
                     fortune will give you a new zest for life.

                     If considering a new love affair, new employment, a career
                     change, or you wish to travel, then go for it.

                     You may also receive an unexpected gift!""",
    },
    "The Moon": {
        "Aurora": """Despite the fear and bewilderment you feel, and the seeming
                     difficulty of the path you have chosen, keep going - all
                     will eventually turn out fine.

                     The Moon is a good omen if you are in a clandestine affair;
                     it also shows us how to be open to new and unexpected
                     possibilities.""",
    },
    "The Sun": {
        "Aurora": """The Sun is shining on you - it's your time for success, joy
                     and happiness.

                     You will feel confident and full of vitality.

                     It's a time to celebrate with friends and loved ones,
                     perhaps enjoy a well-earned holiday, a time of pleasure and
                     good news around children or the conception or birth of a
                     longed-for baby.

                     If you are not feeling this way take heart, you will enter
                     this period soon.""",
    },
    "Judgement": {
        "Aurora": """Brand new potential, an opportunity which once given must
                     not be ignored, a new project, decision or relationship
                     that could affect the rest of your life - all are indicated
                     here.

                     You will enjoy success and enjoyment for past efforts,
                     events will pick up a pace and the outcome will be quicker
                     than expected.""",
    },
    "The World": {
        "Aurora": """Success, fulfillment and conclusion are near at hand - the
                     successful outcome to a venture, satisfaction in a
                     relationship and efforts rewarded.

                     This culmination of events indicates material wealth and
                     greater spiritual awareness. You may choose to buy that
                     dream house or a wonderfully fulfilling relationship is on
                     offer.

                     Enjoy!""",
    },
}
# }}}
# {{{ majorarcana_card5
majorarcana_card5 = {
    "The Fool": {
        "Aurora": """Beware of impetuous and impulsive decisions, they could
                     cost you dearly.

                     Draw on your knowledge and experience. Perhaps there are
                     naive and immature beliefs behind your current desires.

                     Are you looking to move onwards and upwards or run away?
                     Look before you leap, you don't want to appear the fool do
                     you?""",
    },
    "The Magician": {
        "Aurora": """Someone, most likely male, isn't quite who they seem.

                     Trickery and deception can be cleverly disguised as charm
                     and friendliness, so be sure that this person does have
                     your best interests at heart.

                     If someone who you feel wary of is presenting you with a
                     business opportunity, be cautious and trust your
                     instincts.""",
    },
    "The High Priestess": {
        "Aurora": """Insecurity is a devil that taunts us, but only if we listen
                     to that 'doubting Thomas' we all have in our heads.

                     Ignore it.

                     What do your instincts tell you? Perhaps you don't like
                     what they say. Well you could always go against your
                     intuition - but we all know what that leads to, don't
                     we!""",
    },
    "The Empress": {
        "Aurora": """There are conflicts around you, frustrations and possibly a
                     breakup in a relationship.

                     Be careful not to overreact and become too protective or
                     dictatorial about your needs, and whatever you do, do not
                     resort to emotional blackmail - it won't do you any
                     favours.

                     You may be experiencing infertility problems or an
                     unplanned pregnancy. If so just know that there are people
                     around you who love and care for you and will provide
                     support.""",
    },
    "The Emperor": {
        "Aurora": """You may be overambitious at this time.

                     Success may remain just out of your reach for a while.

                     Are you being assertive and positive enough? Or are you
                     using aggressive, bullying tactics to no avail?

                     Do not misuse your authority.

                     If you have requested help from a strong, successful man
                     don't let him bully you - he either helps or leaves you to
                     get on with things yourself.""",
    },
    "The Hierophant": {
        "Aurora": """You are simply struggling to conform to others expectations
                     of you and everybody has an opinion of what you should do.

                     Perhaps you are having a crisis of faith and are unsettled
                     at a very spiritual level. Ask yourself who you really are.
                     What is important to you? What makes you happy?

                     Seek out advice or wise counsel if you wish, but accepting
                     who you really are and going after what you want instead of
                     what others want for you is the most important.""",
    },
    "The Lovers": {
        "Aurora": """Are you suffering in silence in an unhappy relationship or
                     feeling very lonely?

                     Do you have the courage to make the decision you really
                     know you should make? You have a great sense of duty, but
                     are you happy?

                     A difficult decision has to be made - have courage and you
                     will achieve emotional happiness.""",
    },
    "The Chariot": {
        "Aurora": """Watch out for being too arrogant or letting that ego of
                     yours get overinflated. Nobody likes a know it all.

                     Watch that temper too. Aggressive bullying behaviour will
                     only set you back. If this doesn't sound like you, beware
                     of someone like this who could set you back.

                     This is a time of movement and change, and conflicts ending
                     in victory, so don't give up.""",
    },
    "Strength": {
        "Aurora": """Your negativity and lack of self-control are your real
                     enemies.

                     If you are finding certain addictions in your life are
                     taking a hold, be it smoking or drinking for example, look
                     inward for your heart's true strength and self-belief.

                     Change your attitude and be positive and you will reap
                     great rewards.""",
    },
    "The Hermit": {
        "Aurora": """You are at risk of doing something hasty out of impatience
                     and rage.

                     This is not a time for irrational and impulsive behaviour -
                     don't be cantankerous (if closer to old than young!) or
                     arrogant and resentful (if closer to young than old!) Try
                     and remain calm and let the rage go. Take time to make a
                     cool and collected decision.

                     The Hermit signals a warning not to make hasty
                     decisions.""",
    },
    "Wheel of Fortune": {
        "Aurora": """A run of bad luck here, perhaps already evident or there
                     are certainly signs that things are not going your way.

                     The responsibility of important decisions weighs heavy with
                     you where there are choices to make. Trust your intuition,
                     and even if you have to make the painful decision to give
                     up something in order to move on, then have the courage to
                     do it.

                     Trust that The Wheel of Fortune constantly turns and whilst
                     it may be against you at the moment, it will in time turn
                     and bring you good fortune.""",
    },
    "Justice": {
        "Aurora": """Things just aren't going your way.

                     Even if you are in the right or the victim of foul play you
                     won't win this one.

                     Take care of whose advice you take and beware of being
                     motivated solely by self-interest.""",
    },
    "The Hanged Man": {
        "Aurora": """You are allowing yourself to be victimised and emotionally
                     blackmailed by others or you're playing the martyr or
                     victim to try to manipulate others.

                     Don't be too materialistic or try and hang onto someone or
                     something for all the wrong reasons.

                     Someone or something has to go. You must find the ability
                     to let go and give this up - don't worry it will turn out
                     for the better for you.""",
    },
    "Death": {
        "Aurora": """This is a period of anxiety, depression and fear with all
                     the turmoil and distressing events happening in your life.

                     It's time to show what you are made of.

                     What has now come to an end leaves room for brand new
                     beginnings in life, love and career. However radical events
                     may be in your life, believe that life goes on and life is
                     what you make of it.""",
    },
    "Temperance": {
        "Aurora": """Life will seem hectic and full of challenges and you will
                     find it hard to have the right perspective on things.

                     You may have a rival in love or at work. Think about
                     whether the relationship or the job is really right for
                     you.

                     This is a time for being calm and patient and life will
                     soon have a sense of normality again.""",
    },
    "The Devil": {
        "Aurora": """It's like you're in a drug-induced haze - it feels great
                     and always leaves you wanting more.

                     This is addiction pure and simple, whether it's an
                     obsessive sexual relationship, money deals that are too
                     good to be true, materialism at any cost or recreational
                     drugs.

                     Take care - these pursuits won't lead to a happy
                     ending.""",
    },
    "The Tower": {
        "Aurora": """However hard you try to control events they just won't go
                     your way.

                     Unexpected challenges, upheaval and dissapointment will
                     bring expectations to an end.

                     Subconsciously you may have wanted a solution - you just
                     didn't expect it to happen this way.

                     Use this period of change as an opportunity for a new
                     beginning.

                     If you have been planning to move home you will be
                     experiencing setbacks.""",
    },
    "The Star": {
        "Aurora": """This is a period of tension and frustrations: you feel
                     pessimistic and fearful that your hopes will be dashed.

                     Any bad luck you may be having is primarily down to your
                     self-doubt and negativity.

                     Have faith that your luck will change.""",
    },
    "The Moon": {
        "Aurora": """You are frozen with fear, lacking nerve and confused as
                     to what it is you actually want.

                     You are allowing all your fears and anxieties to hold you
                     back when you should be opening your mind to new and
                     unexpected possibilities.

                     You do need to be careful however, as there are deceitful
                     people around who may seem charming but are only out for
                     their own gains. If in a clandestine affair beware, your
                     secret may be exposed.""",
    },
    "The Sun": {
        "Aurora": """You may experience a few delays on your quest for success
                     and achievement but don't worry, you'll get there in a
                     blaze of glory.

                     Success may go to your head a little, so a bit of modesty
                     wouldn't go amiss. Other than a few minor delays, look
                     forward to a period of joy and happiness.

                     If you are experiencing problems with conceiving a baby,
                     The Sun often heralds good news around children and a much
                     wanted pregnancy or birth of a longed-for baby.""",
    },
    "Judgement": {
        "Aurora": """If you allow fear to stop you from taking a chance or a new
                     possibility then you will lose out.

                     Do not ignore the new opportunities being presented to you
                     - a decision, new job or relationship could change your
                     life for the better. Do not refuse change when change at
                     this time is vital - feel the fear and do it anyway.

                     Outcomes may well be delayed. However, this is a time for
                     positive action and not passiveness.""",
    },
    "The World": {
        "Aurora": """As always, fear holds us back and so often leads to missed
                     opportunities.

                     Do not give up or change direction this late in the game
                     just because you have experienced delays.

                     Stick with your plan, have faith and trust the universe,
                     and you will reach the successful conclusion you are
                     wanting.""",
    },
}
# }}}
# {{{ majorarcana_card6
majorarcana_card6 = {
    "The Fool": {
        "Aurora": """Open your mind and soul to new possibilities.

                     This is a time to realise your full potential, follow your
                     instincts and act on your hunches - a time for spontaneity,
                     fun and surprises.

                     However, be mindful of being too impulsive. Your decisions
                     should be based on experience and knowledge of self.""",
    },
    "The Magician": {
        "Aurora": """This is a period of positive action with great potential.
                     You are full of self-belief, feeling very empowered and
                     will have the ability to think on your feet.

                     The Magician is an excellent omen for success: it's time to
                     show everyone exactly what you're made of.""",
    },
    "The High Priestess": {
        "Aurora": """Your intuitive powers are at their height at this moment in
                     time; only by listening carefully and trusting them
                     completely can you embrace that power.

                     Do this and you will make strong, clear, self-assured
                     decisions.

                     Allow for flexibility and expect promising outcomes.""",
    },
    "The Empress": {
        "Aurora": """This is a truly creative and fertile time.

                     Expect the best if you are considering having a child,
                     creating a new job or business opportunity or starting a
                     creative project.

                     The Empress symbolizes abundance, joy and happiness, and
                     reassurance - a firm foundation for future progress.""",
    },
    "The Emperor": {
        "Aurora": """Expect success and achievement of your goals: this is a
                     time for fulfillment of your ambitions.

                     If you have placed your trust in your father,
                     husband/partner or another man of significance in your
                     life, they will come up trumps for you.

                     If you have been the victim of ill-will, don't worry, you
                     will win in the end.""",
    },
    "The Hierophant": {
        "Aurora": """Help is at hand. If you want wise counsel and moral
                     guidance put your trust in someone you have a lot of
                     respect for.

                     Don't allow others to influence you too much with what they
                     want you to conform to - be true to yourself.

                     When considering your options, go with tried and tested
                     traditional values, rather than the unconventional novel
                     approach. For example, marriage is more likely to be your
                     desire than a living-together situation.""",
    },
    "The Lovers": {
        "Aurora": """Love is coming into your life even if you really can't
                     see where from at this time.

                     If you are on your own a new lover will soon enter your
                     life.

                     If you are in an unhappy relationship you have a choice to
                     make - go with your heart, take the risk. Greater happiness
                     is ahead of you.""",
    },
    "The Chariot": {
        "Aurora": """Conflicts ending in victory!

                     Keep charging ahead - this is a time of change, travel and
                     success if you stay committed to achieving your goals.

                     A journey relating to work is imminent and if you've had
                     your eye on that new car it will soon be yours.""",
    },
    "Strength": {
        "Aurora": """Courage and self-belief is what you need to succeed. You may
                     already feel overflowing with these, and if so there's no
                     doubt you will achieve what you want with your career,
                     finances and love life.

                     If you are feeling negative, look inward for that strength
                     and courage, you know you are capable of having self-belief
                     and you'll reap great rewards.""",
    },
    "The Hermit": {
        "Aurora": """This is a time for you to be alone or may herald a time of
                     loneliness. Take this time for quiet introspection and
                     rest.

                     Don't worry, you will find the answers, but the Hermit
                     signals a warning not to make hasty decisions.

                     If you have been unwell this is a time for rest and
                     recuperation.""",
    },
    "Wheel of Fortune": {
        "Aurora": """Expect life to change - and quickly.

                     Fate, destiny or synchronicity, call it what you like,
                     positive change and good fortune is evident here.

                     If you have important choices to make trust your intuition.
                     Do you feel that events seem to be evolving without much
                     input from you? If so trust it and go with the flow.""",
    },
    "Justice": {
        "Aurora": """Justice will be done.

                     Decisions will go in your favor, particularly regarding
                     partnerships or legal matters.

                     Now is the time for some good luck and reward for your good
                     deeds in the past.""",
    },
    "The Hanged Man": {
        "Aurora": """You will in time know what decision to make about who or
                     what must be given up. This is a time of passage from one
                     phase of your life to another.

                     It may be a difficult choice, and self-sacrifice is never
                     easy, but if you look for truth and integrity and don't be
                     too materialistic or hang onto things or people for all the
                     wrong reasons, everything will turn out in your favour.""",
    },
    "Death": {
        "Aurora": """This is a transformational time for you.

                     However turbulent or perhaps distressing some of the events
                     in your life may be, endings always leave room for brand
                     new beginnings.

                     This is a fresh start in life for you, embrace it and live
                     every day as though it were your last - life is for
                     living!""",
    },
    "Temperance": {
        "Aurora": """A period of peace and harmony, life will flow and you will
                     find a way of handling any difficult circumstances with
                     calm confidence.

                     This is also a time for patience, so if you are not sure
                     quite what decision to make about any key issue, take your
                     time. You'll know what to do when the time is right.""",
    },
    "The Devil": {
        "Aurora": """If your previous cards have been positive and your main
                     consideration has been about a relationship then there's a
                     possibility of commitment, even a proposal of marriage.

                     If this is not the case, there is a final opportunity for
                     you to change course, because the temptation you are
                     experiencing concerning a relationship, money or
                     materialism or any other kind of addiction won't lead to a
                     happy ending.

                     If you are feeling low in self-belief and self-worth and
                     doubt your abilities, don't. Have more confidence - it's
                     not too late to change direction.""",
    },
    "The Tower": {
        "Aurora": """A period of dramatic change and upheaval - however this
                     period of change will herald a new beginning.

                     It is time to re-evaluate. Sometimes, as difficult as the
                     disappointment has been to take, change can create new
                     possibilities you never dreamed of.

                     There could be problems relating to your property, or if
                     considering a new property or move, progress will be
                     thwarted.""",
    },
    "The Star": {
        "Aurora": """This is a time of good luck and fortune, perhaps after a
                     period of struggle and heartache.

                     Good health, possibly after a time of illness, and good
                     fortune will give you a new zest for life.

                     If considering a new love affair, new job, career change,
                     or travel, then go for it.

                     You may also receive a gift or gifts!""",
    },
    "The Moon": {
        "Aurora": """Whilst you are confused and fearful and allowing your
                     anxieties to hold you back, trust that all will turn out
                     well in the end.

                     Things may seem tough or confusing but stick with it, it's
                     right for you.

                     The Moon is a good omen if you are in a clandestine affair
                     and helps guide you to open your mind to new and unexpected
                     possibilities.""",
    },
    "The Sun": {
        "Aurora": """The Sun is shining on you - it's your time for success,
                     joy and happiness. You will feel confident and full of
                     vitality.

                     It's a time to celebrate with friends and loved ones,
                     perhaps enjoy a well-earned holiday, a time of pleasure and
                     good news around children or the conception or birth of a
                     longed-for baby.

                     If you are not feeling this way take heart, you will enter
                     this period soon.""",
    },
    "Judgement": {
        "Aurora": """A time for taking stock, an end to an era or phase of your
                     life and brand new opportunities appearing.

                     An opportunity will present itself that must not be ignored
                     and it could have far-reaching implications, changing your
                     life for the better.

                     You will enjoy success and enjoyment for past efforts,
                     events will pick up a pace and the outcome will be quicker
                     than expected.""",
    },
    "The World": {
        "Aurora": """Success, fulfillment and conclusion are near at hand - the
                     successful outcome to a venture, satisfaction in a
                     relationship and efforts rewarded.

                     It is a culmination of events and indicates material wealth
                     and greater spiritual awareness.

                     You may decide to purchase your dream house, act upon a
                     wonderfully-fulfilling relationship offer or embark on a
                     self-actualization journey.

                     Enjoy!""",
    },
}
# }}}

majorarcana_readings = [
    majorarcana_card1,
    majorarcana_card2,
    majorarcana_card3,
    majorarcana_card4,
    majorarcana_card5,
    majorarcana_card6,
]
