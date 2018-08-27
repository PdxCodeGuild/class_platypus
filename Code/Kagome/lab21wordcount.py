file=open("1338.txt.utf-8.txt","r")
wordcount={}
for word in file.read().split():
    if word not in wordcount:
        wordcount[word] = 1
    else:
        wordcount[word] += 1
print (word,wordcount)
file.close()



Text = '''

"The Project Gutenberg eBook, Selected Prose of Oscar Wilde, by Oscar
Wilde, Edited by Robert Ross


This eBook is for the use of anyone anywhere at no cost and with
almost no restrictions whatsoever.  You may copy it, give it away or
re-use it under the terms of the Project Gutenberg License included
with this eBook or online at www.gutenberg.net





Title: Selected Prose of Oscar Wilde
       with a Preface by Robert Ross


Author: Oscar Wilde

Release Date: March 22, 2005  [eBook #1338]

Language: English

Character set encoding: ISO-646-US (US-ASCII)


***START OF THE PROJECT GUTENBERG EBOOK SELECTED PROSE OF OSCAR WILDE***





Transcribed from the 1914 Methuen and Co. edition by David Price, email
ccx074@coventry.ac.uk





SELECTED PROSE OF OSCAR WILDE


Contents:

Preface by Robert Ross
How They Struck a Contemporary
The Quality of George Meredith
Life in the Fallacious Model
Life the Disciple
Life the Plagiarist
The Indispensable East
The Influence of the Impressionists on Climate
An Exposure to Naturalism
Thomas Griffiths Wainewright
Wainewright at Hobart Town
Cardinal Newman and the Autobiographers
Robert Browning
The Two Supreme and Highest Arts
The Secrets of Immortality
The Critic and his Material
Dante the Living Guide
The Limitations of Genius
Wanted A New Background
Without Frontiers
The Poetry of Archaeology
The Art of Archaeology
Herod Suppliant
The Tetrarch's Remorse
The Tetrarch's Treasure
Salome anticipates Dr. Strauss
The Young King
A Coronation
The King of Spain
A Bull Fight
The Throne Room
A Protected Country
The Blackmailing of the Emperor
Covent Garden
A Letter from Miss Jane Percy to her Aunt
The Triumph of American 'Humor'
The Garden of Death
An Eton Kit-cat
Mrs. Erlynne Exercises the Prerogative of a Grandmother
Motherhood more than Marriage
The Damnable Ideal
From a Rejected Prize-essay
The Possibilities of the Useful
The Artist
The Doer of Good
The Disciple
The Master
The House of Judgment
The Teacher of Wisdom
Wilde gives directions about 'De Profundis'
Carey Street
Sorrow wears no mask
Vita Nuova
The Grand Romantic
Clapham Junction
The Broken Resolution
Domesticity at Berneval
A visit to the Pope




DEDICATION


This anthology is dedicated to Michael Lykiardopulos as a little token of
his services to English Literature in the great Russian Empire.




PREFACE


With the possible exceptions of the Greek Anthology, the "Golden
Treasury" and those which bear the name of E. V. Lucas, no selections of
poetry or prose have ever given complete satisfaction to anyone except
the compiler.  But critics derive great satisfaction from pointing out
errors of omission and inclusion on the part of the anthologist, and all
of us have putatively re-arranged and re-edited even the "Golden
Treasury" in our leisure moments.  In an age when "Art for Art's sake" is
an exploded doctrine, anthologies, like everything else, must have a
purpose.  The purpose or object of the present volume is to afford
admirers of Wilde's work the same innocent pleasure obtainable from
similar compilations, namely that of reconstructing a selection of their
own in their mind's eye--for copyright considerations would interfere
with the materialisation of their dream.

A stray observation in an esteemed weekly periodical determined the plan
of this anthology and the choice of particular passages.  The writer,
whose name has escaped me, opined that the reason the works of Pater and
Wilde were no longer read was owing to both authors having treated
English as a dead language.  By a singular coincidence I had purchased
simultaneously with the newspaper a shilling copy of Pater's
"Renaissance," published by Messrs. Macmillan; and a few days afterwards
Messrs. Methuen issued at a shilling the twenty-eighth edition of "De
Profundis."  Obviously either Messrs. Macmillan and Messrs. Methuen or
the authority on dead languages must have been suffering from
hallucinations.  It occurred to me that a selection of Wilde's prose
might at least rehabilitate the notorious reputation for common sense
enjoyed by all publishers, who rarely issue shilling editions of deceased
authors for mere aesthetic considerations.  And I confess to a hope that
this volume may reach the eye or ear of those who have not read Wilde's
books, or of those, such as Mr. Sydney Grundy, who are irritated by the
revival of his plays and the praise accorded to his works throughout the
Continent.

Wilde's prose is distinguished by its extraordinary ease and clarity, and
by the absence--very singular in his case--of the preciosity which he
admired too much in other writers, and advocated with over-emphasis.
Perhaps that is why many of his stories and essays and plays are used as
English text-books in Russian and Scandinavian and Hungarian schools.
Artifice and affectation, often assumed to be recurrent defects in his
writings by those unacquainted with them, are comparatively rare.  Wilde
once boasted in an interview that only Flaubert, Pater, Keats, and
Maeterlinck had influenced him, and then added in a characteristic way:
"But I had already gone more than half-way to meet them."  Anyone curious
as to the origin of Wilde's style and development should consult the
learned treatise {1} of Dr. Ernst Bendz, whose comprehensive treatment of
the subject renders any elucidation of mine superfluous; while nothing
can be added to Mr. Holbrook Jackson's masterly criticism {2} of Wilde
and his position in literature.

In making this selection, with the valuable assistance of Mr. Stuart
Mason, I have endeavoured to illustrate and to justify the critical
appreciations of both Dr. Bendz and Mr. Holbrook Jackson, as well as to
afford the general reader a fair idea of Wilde's variety as a prose
writer.  He is more various than almost any author of the last century,
though the act of writing was always a burden to him.  Some critic
acutely pointed out that poetry and prose were almost side-issues for
him.  The resulting faults and weakness of what he left are obvious.
Except in the plays he has no sustained scheme of thought.  Even "De
Profundis" is too desultory.

For the purpose of convenient reference I have exercised the prerogative
of a literary executor and editor by endowing with special titles some of
the pieces quoted in these pages.  Though unlike one of Wilde's other
friends I cannot claim to have collaborated with him or to have assisted
him in any of his plays, I was sometimes permitted, as Wilde acknowledges
in different letters, to act in the capacity of godfather by suggesting
the actual titles by which some of his books are known to the world.  I
mention the circumstance only as a precedent for my present temerity.  To
compensate those who disapprove of my choice, I have included two
unpublished letters.  The examples of Wilde's epistolary style, published
since his death, have been generally associated with disagreeable
subjects.  Those included here will, I hope, prove a pleasant contrast.

ROBERT ROSS




HOW THEY STRUCK A CONTEMPORARY


There is such a thing as robbing a story of its reality by trying to make
it too true, and _The Black Arrow_ is so inartistic as not to contain a
single anachronism to boast of, while the transformation of Dr. Jekyll
reads dangerously like an experiment out of the _Lancet_.  As for Mr.
Rider Haggard, who really has, or had once, the makings of a perfectly
magnificent liar, he is now so afraid of being suspected of genius that
when he does tell us anything marvellous, he feels bound to invent a
personal reminiscence, and to put it into a footnote as a kind of
cowardly corroboration.  Nor are our other novelists much better.  Mr.
Henry James writes fiction as if it were a painful duty, and wastes upon
mean motives and imperceptible 'points of view' his neat literary style,
his felicitous phrases, his swift and caustic satire.  Mr. Hall Caine, it
is true, aims at the grandiose, but then he writes at the top of his
voice.  He is so loud that one cannot bear what he says.  Mr. James Payn
is an adept in the art of concealing what is not worth finding.  He hunts
down the obvious with the enthusiasm of a short-sighted detective.  As
one turns over the pages, the suspense of the author becomes almost
unbearable.  The horses of Mr. William Black's phaeton do not soar
towards the sun.  They merely frighten the sky at evening into violent
chromolithographic effects.  On seeing them approach, the peasants take
refuge in dialect.  Mrs. Oliphant prattles pleasantly about curates, lawn-
tennis parties, domesticity, and other wearisome things.  Mr. Marion
Crawford has immolated himself upon the altar of local colour.  He is
like the lady in the French comedy who keeps talking about "le beau ciel
d'Italie."  Besides, he has fallen into the bad habit of uttering moral
platitudes.  He is always telling us that to be good is to be good, and
that to be bad is to be wicked.  At times he is almost edifying.  _Robert
Elsmere_ is of course a masterpiece--a masterpiece of the "genre
ennuyeux," the one form of literature that the English people seems
thoroughly to enjoy.  A thoughtful young friend of ours once told us that
it reminded him of the sort of conversation that goes on at a meat tea in
the house of a serious Nonconformist family, and we can quite believe it.
Indeed it is only in England that such a book could be produced.  England
is the home of lost ideas.  As for that great and daily increasing school
of novelists for whom the sun always rises in the East-End, the only
thing that can be said about them is that they find life crude, and leave
it raw.--_The Decay of Lying_.




THE QUALITY OF GEORGE MEREDITH


Ah!  Meredith!  Who can define him?  His style is chaos illumined by
flashes of lightning.  As a writer he has mastered everything except
language: as a novelist he can do everything, except tell a story: as an
artist he is everything except articulate.  Somebody in
Shakespeare--Touchstone, I think--talks about a man who is always
breaking his shins over his own wit, and it seems to me that this might
serve as the basis for a criticism of Meredith's method.  But whatever he
is, he is not a realist.  Or rather I would say that he is a child of
realism who is not on speaking terms with his father.  By deliberate
choice he has made himself a romanticist.  He has refused to bow the knee
to Baal, and after all, even if the man's fine spirit did not revolt
against the noisy assertions of realism, his style would be quite
sufficient of itself to keep life at a respectful distance.  By its means
he has planted round his garden a hedge full of thorns, and red with
wonderful roses.  As for Balzac, he was a most remarkable combination of
the artistic temperament with the scientific spirit.  The latter he
bequeathed to his disciples.  The former was entirely his own.  The
difference between such a book as M. Zola's _L'Assommoir_ and Balzac's
_Illusions Perdues_ is the difference between unimaginative realism and
imaginative reality.  'All Balzac's characters;' said Baudelaire, 'are
gifted with the same ardour of life that animated himself.  All his
fictions are as deeply coloured as dreams.  Each mind is a weapon loaded
to the muzzle with will.  The very scullions have genius.'  A steady
course of Balzac reduces our living friends to shadows, and our
acquaintances to the shadows of shades.  His characters have a kind of
fervent fiery-coloured existence.  They dominate us, and defy scepticism.
One of the greatest tragedies of my life is the death of Lucien de
Rubempre.  It is a grief from which I have never been able completely to
rid myself.  It haunts me in my moments of pleasure.  I remember it when
I laugh.  But Balzac is no more a realist than Holbein was.  He created
life, he did not copy it.  I admit, however, that he set far too high a
value on modernity of form, and that, consequently, there is no book of
his that, as an artistic masterpiece, can rank with _Salammbo_ or
_Esmond_, or _The Cloister and the Hearth_, or the _Vicomte de
Bragelonne_.--_The Decay of Lying_.




LIFE THE FALLACIOUS MODEL


Art begins with abstract decoration, with purely imaginative and
pleasurable work dealing with what is unreal and non-existent.  This is
the first stage.  Then Life becomes fascinated with this new wonder, and
asks to be admitted into the charmed circle.  Art takes life as part of
her rough material, recreates it, and refashions it in fresh forms, is
absolutely indifferent to fact, invents, imagines, dreams, and keeps
between herself and reality the impenetrable barrier of beautiful style,
of decorative or ideal treatment.  The third stage is when Life gets the
upper hand, and drives Art out into the wilderness.  That is the true
decadence, and it is from this that we are now suffering.

Take the case of the English drama.  At first in the hands of the monks
Dramatic Art was abstract, decorative and mythological.  Then she
enlisted Life in her service, and using some of life's external forms,
she created an entirely new race of beings, whose sorrows were more
terrible than any sorrow man has ever felt, whose joys were keener than
lover's joys, who had the rage of the Titans and the calm of the gods,
who had monstrous and marvellous sins, monstrous and marvellous virtues.
To them she gave a language different from that of actual use, a language
full of resonant music and sweet rhythm, made stately by solemn cadence,
or made delicate by fanciful rhyme, jewelled with wonderful words, and
enriched with lofty diction.  She clothed her children in strange raiment
and gave them masks, and at her bidding the antique world rose from its
marble tomb.  A new Caesar stalked through the streets of risen Rome, and
with purple sail and flute-led oars another Cleopatra passed up the river
to Antioch.  Old myth and legend and dream took shape and substance.
History was entirely re-written, and there was hardly one of the
dramatists who did not recognise that the object of Art is not simple
truth but complex beauty.  In this they were perfectly right.  Art itself
is really a form of exaggeration; and selection, which is the very spirit
of art, is nothing more than an intensified mode of over-emphasis.

But Life soon shattered the perfection of the form.  Even in Shakespeare
we can see the beginning of the end.  It shows itself by the gradual
breaking-up of the blank-verse in the later plays, by the predominance
given to prose, and by the over-importance assigned to characterisation.
The passages in Shakespeare--and they are many--where the language is
uncouth, vulgar, exaggerated, fantastic, obscene even, are entirely due
to Life calling for an echo of her own voice, and rejecting the
intervention of beautiful style, through which alone should life be
suffered to find expression.  Shakespeare is not by any means a flawless
artist.  He is too fond of going directly to life, and borrowing life's
natural utterance.  He forgets that when Art surrenders her imaginative
medium she surrenders everything.--_The Decay of Lying_.




LIFE THE DISCIPLE


We have all seen in our own day in England how a certain curious and
fascinating type of beauty, invented and emphasised by two imaginative
painters, has so influenced Life that whenever one goes to a private view
or to an artistic salon one sees, here the mystic eyes of Rossetti's
dream, the long ivory throat, the strange square-cut jaw, the loosened
shadowy hair that he so ardently loved, there the sweet maidenhood of
'The Golden Stair,' the blossom-like mouth and weary loveliness of the
'Laus Amoris,' the passion-pale face of Andromeda, the thin hands and
lithe beauty of the Vivian in 'Merlin's Dream.'  And it has always been
so.  A great artist invents a type, and Life tries to copy it, to
reproduce it in a popular form, like an enterprising publisher.  Neither
Holbein nor Vandyck found in England what they have given us.  They
brought their types with them, and Life with her keen imitative faculty
set herself to supply the master with models.  The Greeks, with their
quick artistic instinct, understood this, and set in the bride's chamber
the statue of Hermes or of Apollo, that she might bear children as lovely
as the works of art that she looked at in her rapture or her pain.  They
knew that Life gains from art not merely spirituality, depth of thought
and feeling, soul-turmoil or soul-peace, but that she can form herself on
the very lines and colours of art, and can reproduce the dignity of
Pheidias as well as the grace of Praxiteles.  Hence came their objection
to realism.  They disliked it on purely social grounds.  They felt that
it inevitably makes people ugly, and they were perfectly right.  We try
to improve the conditions of the race by means of good air, free
sunlight, wholesome water, and hideous bare buildings for the better
housing of the lower orders.  But these things merely produce health,
they do not produce beauty.  For this, Art is required, and the true
disciples of the great artist are not his studio-imitators, but those who
become like his works of art, be they plastic as in Greek days, or
pictorial as in modern times; in a word, Life is Art's best, Art's only
pupil.--_The Decay of Lying_.




LIFE THE PLAGIARIST


I once asked a lady, who knew Thackeray intimately, whether he had had
any model for Becky Sharp.  She told me that Becky was an invention, but
that the idea of the character had been partly suggested by a governess
who lived in the neighbourhood of Kensington Square, and was the
companion of a very selfish and rich old woman.  I inquired what became
of the governess, and she replied that, oddly enough, some years after
the appearance of _Vanity Fair_, she ran away with the nephew of the lady
with whom she was living, and for a short time made a great splash in
society, quite in Mrs. Rawdon Crawley's style, and entirely by Mrs.
Rawdon Crawley's methods.  Ultimately she came to grief, disappeared to
the Continent, and used to be occasionally seen at Monte Carlo and other
gambling places.  The noble gentleman from whom the same great
sentimentalist drew Colonel Newcome died, a few months after _The
Newcomer_ had reached a fourth edition, with the word 'Adsum' on his
lips.  Shortly after Mr. Stevenson published his curious psychological
story of transformation, a friend of mine, called Mr. Hyde, was in the
north of London, and being anxious to get to a railway station, took what
he thought would be a short cut, lost his way, and found himself in a
network of mean, evil-looking streets.  Feeling rather nervous he began
to walk extremely fast, when suddenly out of an archway ran a child right
between his legs.  It fell on the pavement, he tripped over it, and
trampled upon it.  Being of course very much frightened and a little
hurt, it began to scream, and in a few seconds the whole street was full
of rough people who came pouring out of the houses like ants.  They
surrounded him, and asked him his name.  He was just about to give it
when he suddenly remembered the opening incident in Mr. Stevenson's
story.  He was so filled with horror at having realised in his own person
that terrible and well-written scene, and at having done accidentally,
though in fact, what the Mr. Hyde of fiction had done with deliberate
intent, that he ran away as hard as he could go.  He was, however, very
closely followed, and finally he took refuge in a surgery, the door of
which happened to be open, where he explained to a young assistant, who
happened to be there, exactly what had occurred.  The humanitarian crowd
were induced to go away on his giving them a small sum of money, and as
soon as the coast was clear he left.  As he passed out, the name on the
brass door-plate of the surgery caught his eye.  It was 'Jekyll.'  At
least it should have been.--_The Decay of Lying_.




THE INDISPENSABLE EAST


What is true about the drama and the novel is no less true about those
arts that we call the decorative arts.  The whole history of these arts
in Europe is the record of the struggle between Orientalism, with its
frank rejection of imitation, its love of artistic convention, its
dislike to the actual representation of any object in Nature, and our own
imitative spirit.  Wherever the former has been paramount, as in
Byzantium, Sicily and Spain, by actual contact, or in the rest of Europe
by the influence of the Crusades, we have had beautiful and imaginative
work in which the visible things of life are transmuted into artistic
conventions, and the things that Life has not are invented and fashioned
for her delight.  But wherever we have returned to Life and Nature, our
work has always become vulgar, common and uninteresting.  Modern
tapestry, with its aerial effects, its elaborate perspective, its broad
expanses of waste sky, its faithful and laborious realism, has no beauty
whatsoever.  The pictorial glass of Germany is absolutely detestable.  We
are beginning to weave possible carpets in England, but only because we
have returned to the method and spirit of the East.  Our rugs and carpets
of twenty years ago, with their solemn depressing truths, their inane
worship of Nature, their sordid reproductions of visible objects, have
become, even to the Philistine, a source of laughter.  A cultured
Mahomedan once remarked to us, "You Christians are so occupied in
misinterpreting the fourth commandment that you have never thought of
making an artistic application of the second."  He was perfectly right,
and the whole truth of the matter is this: The proper school to learn art
in is not Life but Art.--_The Decay of Lying_.




THE INFLUENCE OF THE IMPRESSIONISTS ON CLIMATE


Where, if not from the Impressionists, do we get those wonderful brown
fogs that come creeping down our streets, blurring the gas-lamps and
changing the houses into monstrous shadows?  To whom, if not to them and
their master, do we owe the lovely silver mists that brood over our
river, and turn to faint forms of fading grace curved bridge and swaying
barge?  The extraordinary change that has taken place in the climate of
London during the last ten years is entirely due to a particular school
of Art.  You smile.  Consider the matter from a scientific or a
metaphysical point of view, and you will find that I am right.  For what
is Nature?  Nature is no great mother who has borne us.  She is our
creation.  It is in our brain that she quickens to life.  Things are
because we see them, and what we see, and how we see it, depends on the
Arts that have influenced us.  To look at a thing is very different from
seeing a thing.  One does not see anything until one sees its beauty.
Then, and then only, does it come into existence.  At present, people see
fogs, not because there are fogs, but because poets and painters have
taught them the mysterious loveliness of such effects.  There may have
been fogs for centuries in London.  I dare say there were.  But no one
saw them, and so we do not know anything about them.  They did not exist
till Art had invented them.  Now, it must be admitted, fogs are carried
to excess.  They have become the mere mannerism of a clique, and the
exaggerated realism of their method gives dull people bronchitis.  Where
the cultured catch an effect, the uncultured catch cold.  And so, let us
be humane, and invite Art to turn her wonderful eyes elsewhere.  She has
done so already, indeed.  That white quivering sunlight that one sees now
in France, with its strange blotches of mauve, and its restless violet
shadows, is her latest fancy, and, on the whole, Nature reproduces it
quite admirably.  Where she used to give us Corots and Daubignys, she
gives us now exquisite Monets and entrancing Pissaros.  Indeed there are
moments, rare, it is true, but still to be observed from time to time,
when Nature becomes absolutely modern.  Of course she is not always to be
relied upon.  The fact is that she is in this unfortunate position.  Art
creates an incomparable and unique effect, and, having done so, passes on
to other things.  Nature, upon the other hand, forgetting that imitation
can be made the sincerest form of insult, keeps on repeating this effect
until we all become absolutely wearied of it.  Nobody of any real
culture, for instance, ever talks nowadays about the beauty of a sunset.
Sunsets are quite old-fashioned.  They belong to the time when Turner was
the last note in art.  To admire them is a distinct sign of provincialism
of temperament.  Upon the other hand they go on.--_The Decay of Lying_.




AN EXPOSURE OF NATURALISM


After all, what the imitative arts really give us are merely the various
styles of particular artists, or of certain schools of artists.  Surely
you don't imagine that the people of the Middle Ages bore any resemblance
at all to the figures on mediaeval stained glass, or in mediaeval stone
and wood carving, or on mediaeval metal-work, or tapestries, or
illuminated MSS.  They were probably very ordinary-looking people, with
nothing grotesque, or remarkable, or fantastic in their appearance.  The
Middle Ages, as we know them in art, are simply a definite form of style,
and there is no reason at all why an artist with this style should not be
produced in the nineteenth century.  No great artist ever sees things as
they really are.  If he did, he would cease to be an artist.  Take an
example from our own day.  I know that you are fond of Japanese things.
Now, do you really imagine that the Japanese people, as they are
presented to us in art, have any existence?  If you do, you have never
understood Japanese art at all.  The Japanese people are the deliberate
self-conscious creation of certain individual artists.  If you set a
picture by Hokusai, or Hokkei, or any of the great native painters,
beside a real Japanese gentleman or lady, you will see that there is not
the slightest resemblance between them.  The actual people who live in
Japan are not unlike the general run of English people; that is to say,
they are extremely commonplace, and have nothing curious or extraordinary
about them.  In fact the whole of Japan is a pure invention.  There is no
such country, there are no such people.  One of our most charming
painters {3} went recently to the Land of the Chrysanthemum in the
foolish hope of seeing the Japanese.  All he saw, all he had the chance
of painting, were a few lanterns and some fans.  He was quite unable to
discover the inhabitants, as his delightful exhibition at Messrs.
Dowdeswell's Gallery showed only too well.  He did not know that the
Japanese people are, as I have said, simply a mode of style, an exquisite
fancy of art.  And so, if you desire to see a Japanese effect, you will
not behave like a tourist and go to Tokio.  On the contrary, you will
stay at home and steep yourself in the work of certain Japanese artists,
and then, when you have absorbed the spirit of their style, and caught
their imaginative manner of vision, you will go some afternoon and sit in
the Park or stroll down Piccadilly, and if you cannot see an absolutely
Japanese effect there, you will not see it anywhere.  Or, to return again
to the past, take as another instance the ancient Greeks.  Do you think
that Greek art ever tells us what the Greek people were like?  Do you
believe that the Athenian women were like the stately dignified figures
of the Parthenon frieze, or like those marvellous goddesses who sat in
the triangular pediments of the same building?  If you judge from the
art, they certainly were so.  But read an authority, like Aristophanes,
for instance.  You will find that the Athenian ladies laced tightly, wore
high-heeled shoes, dyed their hair yellow, painted and rouged their
faces, and were exactly like any silly fashionable or fallen creature of
our own day.  The fact is that we look back on the ages entirely through
the medium of art, and art, very fortunately, has never once told us the
truth.--_The Decay of Lying_.




THOMAS GRIFFITHS WAINEWRIGHT


He was taken back to Newgate, preparatory to his removal to the colonies.
In a fanciful passage in one of his early essays he had fancied himself
'lying in Horsemonger Gaol under sentence of death' for having been
unable to resist the temptation of stealing some Marc Antonios from the
British Museum in order to complete his collection.  The sentence now
passed on him was to a man of his culture a form of death.  He complained
bitterly of it to his friends, and pointed out, with a good deal of
reason, some people may fancy, that the money was practically his own,
having come to him from his mother, and that the forgery, such as it was,
had been committed thirteen years before, which, to use his own phrase,
was at least a _circonstance attenuante_.  The permanence of personality
is a very subtle metaphysical problem, and certainly the English law
solves the question in an extremely rough-and-ready manner.  There is,
however, something dramatic in the fact that this heavy punishment was
inflicted on him for what, if we remember his fatal influence on the
prose of modern journalism, was certainly not the worst of all his sins.

While he was in gaol, Dickens, Macready, and Hablot Browne came across
him by chance.  They had been going over the prisons of London, searching
for artistic effects, and in Newgate they suddenly caught sight of
Wainewright.  He met them with a defiant stare, Forster tells us, but
Macready was 'horrified to recognise a man familiarly known to him in
former years, and at whose table he had dined.'

Others had more curiosity, and his cell was for some time a kind of
fashionable lounge.  Many men of letters went down to visit their old
literary comrade.  But he was no longer the kind light-hearted Janus whom
Charles Lamb admired.  He seems to have grown quite cynical.

To the agent of an insurance company who was visiting him one afternoon,
and thought he would improve the occasion by pointing out that, after
all, crime was a bad speculation, he replied: 'Sir, you City men enter on
your speculations, and take the chances of them.  Some of your
speculations succeed, some fail.  Mine happen to have failed, yours
happen to have succeeded.  That is the only difference, sir, between my
visitor and me.  But, sir, I will tell you one thing in which I have
succeeded to the last.  I have been determined through life to hold the
position of a gentleman.  I have always done so.  I do so still.  It is
the custom of this place that each of the inmates of a cell shall take
his morning's turn of sweeping it out.  I occupy a cell with a bricklayer
and a sweep, but they never offer me the broom!'  When a friend
reproached him with the murder of Helen Abercrombie he shrugged his
shoulders and said, 'Yes; it was a dreadful thing to do, but she had very
thick ankles.'--_Pen, Pencil and Poison_.




WAINEWRIGHT AT HOBART TOWN


His love of art, however, never deserted him.  At Hobart Town he started
a studio, and returned to sketching and portrait-painting, and his
conversation and manners seem not to have lost their charm.  Nor did he
give up his habit of poisoning, and there are two cases on record in
which he tried to make away with people who had offended him.  But his
hand seems to have lost its cunning.  Both of his attempts were complete
failures, and in 1844, being thoroughly dissatisfied with Tasmanian
society, he presented a memorial to the governor of the settlement, Sir
John Eardley Wilmot, praying for a ticket-of-leave.  In it he speaks of
himself as being 'tormented by ideas struggling for outward form and
realisation, barred up from increase of knowledge, and deprived of the
exercise of profitable or even of decorous speech.'  His request,
however, was refused, and the associate of Coleridge consoled himself by
making those marvellous _Paradis Artificiels_ whose secret is only known
to the eaters of opium.  In 1852 he died of apoplexy, his sole living
companion being a cat, for which he had evinced at extraordinary
affection.

His crimes seem to have had an important effect upon his art.  They gave
a strong personality to his style, a quality that his early work
certainly lacked.  In a note to the _Life of Dickens_, Forster mentions
that in 1847 Lady Blessington received from her brother, Major Power, who
held a military appointment at Hobart Town, an oil portrait of a young
lady from his clever brush; and it is said that 'he had contrived to put
the expression of his own wickedness into the portrait of a nice, kind-
hearted girl.'  M. Zola, in one of his novels, tells us of a young man
who, having committed a murder, takes to art, and paints greenish
impressionist portraits of perfectly respectable people, all of which
bear a curious resemblance to his victim.  The development of Mr.
Wainewright's style seems to me far more subtle and suggestive.  One can
fancy an intense personality being created out of sin.--_Pen, Pencil and
Poison_.




CARDINAL NEWMAN AND THE AUTOBIOGRAPHERS


In literature mere egotism is delightful.  It is what fascinates us in
the letters of personalities so different as Cicero and Balzac, Flaubert
and Berlioz, Byron and Madame de Sevigne.  Whenever we come across it,
and, strangely enough, it is rather rare, we cannot but welcome it, and
do not easily forget it.  Humanity will always love Rousseau for having
confessed his sins, not to a priest, but to the world, and the couchant
nymphs that Cellini wrought in bronze for the castle of King Francis, the
green and gold Perseus, even, that in the open Loggia at Florence shows
the moon the dead terror that once turned life to stone, have not given
it more pleasure than has that autobiography in which the supreme
scoundrel of the Renaissance relates the story of his splendour and his
shame.  The opinions, the character, the achievements of the man, matter
very little.  He may be a sceptic like the gentle Sieur de Montaigne, or
a saint like the bitter son of Monica, but when he tells us his own
secrets he can always charm our ears to listening and our lips to
silence.  The mode of thought that Cardinal Newman represented--if that
can be called a mode of thought which seeks to solve intellectual
problems by a denial of the supremacy of the intellect--may not, cannot,
I think, survive.  But the world will never weary of watching that
troubled soul in its progress from darkness to darkness.  The lonely
church at Littlemore, where 'the breath of the morning is damp, and
worshippers are few,' will always be dear to it, and whenever men see the
yellow snapdragon blossoming on the wall of Trinity they will think of
that gracious undergraduate who saw in the flower's sure recurrence a
prophecy that he would abide for ever with the Benign Mother of his
days--a prophecy that Faith, in her wisdom or her folly, suffered not to
be fulfilled.  Yes; autobiography is irresistible.--_The Critic as
Artist_.




ROBERT BROWNING


Taken as a whole the man was great.  He did not belong to the Olympians,
and had all the incompleteness of the Titan.  He did not survey, and it
was but rarely that he could sing.  His work is marred by struggle,
violence and effort, and he passed not from emotion to form, but from
thought to chaos.  Still, he was great.  He has been called a thinker,
and was certainly a man who was always thinking, and always thinking
aloud; but it was not thought that fascinated him, but rather the
processes by which thought moves.  It was the machine he loved, not what
the machine makes.  The method by which the fool arrives at his folly was
as dear to him as the ultimate wisdom of the wise.  So much, indeed, did
the subtle mechanism of mind fascinate him that he despised language, or
looked upon it as an incomplete instrument of expression.  Rhyme, that
exquisite echo which in the Muse's hollow hill creates and answers its
own voice; rhyme, which in the hands of the real artist becomes not
merely a material element of metrical beauty, but a spiritual element of
thought and passion also, waking a new mood, it may be, or stirring a
fresh train of ideas, or opening by mere sweetness and suggestion of
sound some golden door at which the Imagination itself had knocked in
vain; rhyme, which can turn man's utterance to the speech of gods; rhyme,
the one chord we have added to the Greek lyre, became in Robert
Browning's hands a grotesque, misshapen thing, which at times made him
masquerade in poetry as a low comedian, and ride Pegasus too often with
his tongue in his cheek.  There are moments when he wounds us by
monstrous music.  Nay, if he can only get his music by breaking the
strings of his lute, he breaks them, and they snap in discord, and no
Athenian tettix, making melody from tremulous wings, lights on the ivory
horn to make the movement perfect, or the interval less harsh.  Yet, he
was great: and though he turned language into ignoble clay, he made from
it men and women that live.  He is the most Shakespearian creature since
Shakespeare.  If Shakespeare could sing with myriad lips, Browning could
stammer through a thousand mouths.  Even now, as I am speaking, and
speaking not against him but for him, there glides through the room the
pageant of his persons.  There, creeps Fra Lippo Lippi with his cheeks
still burning from some girl's hot kiss.  There, stands dread Saul with
the lordly male-sapphires gleaming in his turban.  Mildred Tresham is
there, and the Spanish monk, yellow with hatred, and Blougram, and Ben
Ezra, and the Bishop of St. Praxed's.  The spawn of Setebos gibbers in
the corner, and Sebald, hearing Pippa pass by, looks on Ottima's haggard
face, and loathes her and his own sin, and himself.  Pale as the white
satin of his doublet, the melancholy king watches with dreamy treacherous
eyes too loyal Strafford pass forth to his doom, and Andrea shudders as
he hears the cousins whistle in the garden, and bids his perfect wife go
down.  Yes, Browning was great.  And as what will he be remembered?  As a
poet?  Ah, not as a poet!  He will be remembered as a writer of fiction,
as the most supreme writer of fiction, it may be, that we have ever had.
His sense of dramatic situation was unrivalled, and, if he could not
answer his own problems, he could at least put problems forth, and what
more should an artist do?  Considered from the point of view of a creator
of character he ranks next to him who made Hamlet.  Had he been
articulate, he might have sat beside him.  The only man who can touch the
hem of his garment is George Meredith.  Meredith is a prose Browning, and
so is Browning. He used poetry as a medium for writing in prose.--_The
Critic as Artist_.




THE TWO SUPREME AND HIGHEST ARTS


Life and Literature, life and the perfect expression of life.  The
principles of the former, as laid down by the Greeks, we may not realise
in an age so marred by false ideals as our own.  The principles of the
latter, as they laid them down, are, in many cases, so subtle that we can
hardly understand them.  Recognising that the most perfect art is that
which most fully mirrors man in all his infinite variety, they elaborated
the criticism of language, considered in the light of the mere material
of that art, to a point to which we, with our accentual system of
reasonable or emotional emphasis, can barely if at all attain; studying,
for instance, the metrical movements of a prose as scientifically as a
modern musician studies harmony and counterpoint, and, I need hardly say,
with much keener aesthetic instinct.  In this they were right, as they
were right in all things.  Since the introduction of printing, and the
fatal development of the habit of reading amongst the middle and lower
classes of this country, there has been a tendency in literature to
appeal more and more to the eye, and less and less to the ear which is
really the sense which, from the standpoint of pure art, it should seek
to please, and by whose canons of pleasure it should abide always.  Even
the work of Mr. Pater, who is, on the whole, the most perfect master of
English prose now creating amongst us, is often far more like a piece of
mosaic than a passage in music, and seems, here and there, to lack the
true rhythmical life of words and the fine freedom and richness of effect
that such rhythmical life produces.  We, in fact, have made writing a
definite mode of composition, and have treated it as a form of elaborate
design.  The Greeks, upon the other hand, regarded writing simply as a
method of chronicling.  Their test was always the spoken word in its
musical and metrical relations.  The voice was the medium, and the ear
the critic.  I have sometimes thought that the story of Homer's blindness
might be really an artistic myth, created in critical days, and serving
to remind us, not merely that the great poet is always a seer, seeing
less with the eyes of the body than he does with the eyes of the soul,
but that he is a true singer also, building his song out of music,
repeating each line over and over again to himself till he has caught the
secret of its melody, chaunting in darkness the words that are winged
with light.  Certainly, whether this be so or not, it was to his
blindness, as an occasion, if not as a cause, that England's great poet
owed much of the majestic movement and sonorous splendour of his later
verse.  When Milton could no longer write he began to sing.--_The Critic
as Artist_.




THE SECRETS OF IMMORTALITY


On the mouldering citadel of Troy lies the lizard like a thing of green
bronze.  The owl has built her nest in the palace of Priam.  Over the
empty plain wander shepherd and goatherd with their flocks, and where, on
the wine-surfaced, oily sea, [Greek text], as Homer calls it,
copper-prowed and streaked with vermilion, the great galleys of the
Danaoi came in their gleaming crescent, the lonely tunny-fisher sits in
his little boat and watches the bobbing corks of his net.  Yet, every
morning the doors of the city are thrown open, and on foot, or in horse-
drawn chariot, the warriors go forth to battle, and mock their enemies
from behind their iron masks.  All day long the fight rages, and when
night comes the torches gleam by the tents, and the cresset burns in the
hall.  Those who live in marble or on painted panel, know of life but a
single exquisite instant, eternal indeed in its beauty, but limited to
one note of passion or one mood of calm.  Those whom the poet makes live
have their myriad emotions of joy and terror, of courage and despair, of
pleasure and of suffering.  The seasons come and go in glad or saddening
pageant, and with winged or leaden feet the years pass by before them.
They have their youth and their manhood, they are children, and they grow
old.  It is always dawn for St. Helena, as Veronese saw her at the
window.  Through the still morning air the angels bring her the symbol of
God's pain.  The cool breezes of the morning lift the gilt threads from
her brow.  On that little hill by the city of Florence, where the lovers
of Giorgione are lying, it is always the solstice of noon, of noon made
so languorous by summer suns that hardly can the slim naked girl dip into
the marble tank the round bubble of clear glass, and the long fingers of
the lute-player rest idly upon the chords.  It is twilight always for the
dancing nymphs whom Corot set free among the silver poplars of France.  In
eternal twilight they move, those frail diaphanous figures, whose
tremulous white feet seem not to touch the dew-drenched grass they tread
on.  But those who walk in epos, drama, or romance, see through the
labouring months the young moons wax and wane, and watch the night from
evening unto morning star, and from sunrise unto sunsetting can note the
shifting day with all its gold and shadow.  For them, as for us, the
flowers bloom and wither, and the Earth, that Green-tressed Goddess as
Coleridge calls her, alters her raiment for their pleasure.  The statue
is concentrated to one moment of perfection.  The image stained upon the
canvas possesses no spiritual element of growth or change.  If they know
nothing of death, it is because they know little of life, for the secrets
of life and death belong to those, and those only, whom the sequence of
time affects, and who possess not merely the present but the future, and
can rise or fall from a past of glory or of shame.  Movement, that
problem of the visible arts, can be truly realised by Literature alone.
It is Literature that shows us the body in its swiftness and the soul in
its unrest.--_The Critic as Artist_.




THE CRITIC AND HIS MATERIAL


Who cares whether Mr. Ruskin's views on Turner are sound or not?  What
does it matter?  That mighty and majestic prose of his, so fervid and so
fiery-coloured in its noble eloquence, so rich in its elaborate symphonic
music, so sure and certain, at its best, in subtle choice of word and
epithet, is at least as great a work of art as any of those wonderful
sunsets that bleach or rot on their corrupted canvases in England's
Gallery; greater indeed, one is apt to think at times, not merely because
its equal beauty is more enduring, but on account of the fuller variety
of its appeal, soul speaking to soul in those long-cadenced lines, not
through form and colour alone, though through these, indeed, completely
and without loss, but with intellectual and emotional utterance, with
lofty passion and with loftier thought, with imaginative insight, and
with poetic aim; greater, I always think, even as Literature is the
greater art.  Who, again, cares whether Mr. Pater has put into the
portrait of Monna Lisa something that Lionardo never dreamed of?  The
painter may have been merely the slave of an archaic smile, as some have
fancied, but whenever I pass into the cool galleries of the Palace of the
Louvre, and stand before that strange figure 'set in its marble chair in
that cirque of fantastic rocks, as in some faint light under sea,' I
murmur to myself, 'She is older than the rocks among which she sits; like
the vampire, she has been dead many times, and learned the secrets of the
grave; and has been a diver in deep seas, and keeps their fallen day
about her: and trafficked for strange webs with Eastern merchants; and,
as Leda, was the mother of Helen of Troy, and, as St. Anne, the mother of
Mary; and all this has been to her but as the sound of lyres and flutes,
and lives only in the delicacy with which it has moulded the changing
lineaments, and tinged the eyelids and the hands.'  And I say to my
friend, 'The presence that thus so strangely rose beside the waters is
expressive of what in the ways of a thousand years man had come to
desire'; and he answers me, 'Hers is the head upon which all "the ends of
the world are come," and the eyelids are a little weary.'

And so the picture becomes more wonderful to us than it really is, and
reveals to us a secret of which, in truth, it knows nothing, and the
music of the mystical prose is as sweet in our ears as was that flute-
player's music that lent to the lips of La Gioconda those subtle and
poisonous curves.  Do you ask me what Lionardo would have said had any
one told him of this picture that 'all the thoughts and experience of the
world had etched and moulded therein that which they had of power to
refine and make expressive the outward form, the animalism of Greece, the
lust of Rome, the reverie of the Middle Age with its spiritual ambition
and imaginative loves, the return of the Pagan world, the sins of the
Borgias?'  He would probably have answered that he had contemplated none
of these things, but had concerned himself simply with certain
arrangements of lines and masses, and with new and curious
colour-harmonies of blue and green.  And it is for this very reason that
the criticism which I have quoted is criticism of the highest kind.  It
treats the work of art simply as a starting-point for a new creation.  It
does not confine itself--let us at least suppose so for the moment--to
discovering the real intention of the artist and accepting that as final.
And in this it is right, for the meaning of any beautiful created thing
is, at least, as much in the soul of him who looks at it, as it was in
his soul who wrought it.  Nay, it is rather the beholder who lends to the
beautiful thing its myriad meanings, and makes it marvellous for us, and
sets it in some new relation to the age, so that it becomes a vital
portion of our lives, and a symbol of what we pray for, or perhaps of
what, having prayed for, we fear that we may receive.--_The Critic as
Artist_.




DANTE THE LIVING GUIDE


There is no mood or passion that Art cannot give us, and those of us who
have discovered her secret can settle beforehand what our experiences are
going to be.  We can choose our day and select our hour.  We can say to
ourselves, 'To-morrow, at dawn, we shall walk with grave Virgil through
the valley of the shadow of death,' and lo! the dawn finds us in the
obscure wood, and the Mantuan stands by our side.  We pass through the
gate of the legend fatal to hope, and with pity or with joy behold the
horror of another world.  The hypocrites go by, with their painted faces
and their cowls of gilded lead.  Out of the ceaseless winds that drive
them, the carnal look at us, and we watch the heretic rending his flesh,
and the glutton lashed by the rain.  We break the withered branches from
the tree in the grove of the Harpies, and each dull-hued poisonous twig
bleeds with red blood before us, and cries aloud with bitter cries.  Out
of a horn of fire Odysseus speaks to us, and when from his sepulchre of
flame the great Ghibelline rises, the pride that triumphs over the
torture of that bed becomes ours for a moment.  Through the dim purple
air fly those who have stained the world with the beauty of their sin,
and in the pit of loathsome disease, dropsy-stricken and swollen of body
into the semblance of a monstrous lute, lies Adamo di Brescia, the coiner
of false coin.  He bids us listen to his misery; we stop, and with dry
and gaping lips he tells us how he dreams day and night of the brooks of
clear water that in cool dewy channels gush down the green Casentine
hills.  Sinon, the false Greek of Troy, mocks at him.  He smites him in
the face, and they wrangle.  We are fascinated by their shame, and
loiter, till Virgil chides us and leads us away to that city turreted by
giants where great Nimrod blows his horn.  Terrible things are in store
for us, and we go to meet them in Dante's raiment and with Dante's heart.
We traverse the marshes of the Styx, and Argenti swims to the boat
through the slimy waves.  He calls to us, and we reject him.  When we
hear the voice of his agony we are glad, and Virgil praises us for the
bitterness of our scorn.  We tread upon the cold crystal of Cocytus, in
which traitors stick like straws in glass.  Our foot strikes against the
head of Bocca.  He will not tell us his name, and we tear the hair in
handfuls from the screaming skull.  Alberigo prays us to break the ice
upon his face that he may weep a little.  We pledge our word to him, and
when he has uttered his dolorous tale we deny the word that we have
spoken, and pass from him; such cruelty being courtesy indeed, for who
more base than he who has mercy for the condemned of God?  In the jaws of
Lucifer we see the man who sold Christ, and in the jaws of Lucifer the
men who slew Caesar.  We tremble, and come forth to re-behold the
stars.--_The Critic as Artist_.




THE LIMITATIONS OF GENIUS


The appeal of all Art is simply to the artistic temperament.  Art does
not address herself to the specialist.  Her claim is that she is
universal, and that in all her manifestations she is one.  Indeed, so far
from its being true that the artist is the best judge of art, a really
great artist can never judge of other people's work at all, and can
hardly, in fact, judge of his own.  That very concentration of vision
that makes a man an artist, limits by its sheer intensity his faculty of
fine appreciation.  The energy of creation hurries him blindly on to his
own goal.  The wheels of his chariot raise the dust as a cloud around
him.  The gods are hidden from each other.  They can recognise their
worshippers.  That is all . . . Wordsworth saw in _Endymion_ merely a
pretty piece of Paganism, and Shelley, with his dislike of actuality, was
deaf to Wordsworth's message, being repelled by its form, and Byron, that
great passionate human incomplete creature, could appreciate neither the
poet of the cloud nor the poet of the lake, and the wonder of Keats was
hidden from him.  The realism of Euripides was hateful to Sophokles.
Those droppings of warm tears had no music for him.  Milton, with his
sense of the grand style, could not understand the method of Shakespeare,
any more than could Sir Joshua the method of Gainsborough.  Bad artists
always admire each other's work.  They call it being large-minded and
free from prejudice.  But a truly great artist cannot conceive of life
being shown, or beauty fashioned, under any conditions other than those
that he has selected.  Creation employs all its critical faculty within
its own sphere.  It may not use it in the sphere that belongs to others.
It is exactly because a man cannot do a thing that he is the proper judge
of it.--_The Critic as Artist_.




WANTED A NEW BACKGROUND


He who would stir us now by fiction must either give us an entirely new
background, or reveal to us the soul of man in its innermost workings.
The first is for the moment being done for us by Mr. Rudyard Kipling.  As
one turns over the pages of his _Plain Tales from the Hills_, one feels
as if one were seated under a palm-tree reading life by superb flashes of
vulgarity.  The bright colours of the bazaars dazzle one's eyes.  The
jaded, second-rate Anglo-Indians are in exquisite incongruity with their
surroundings.  The mere lack of style in the story-teller gives an odd
journalistic realism to what he tells us.  From the point of view of
literature Mr. Kipling is a genius who drops his aspirates.  From the
point of view of life, he is a reporter who knows vulgarity better than
any one has ever known it.  Dickens knew its clothes and its comedy.  Mr.
Kipling knows its essence and its seriousness.  He is our first authority
on the second-rate, and has seen marvellous things through keyholes, and
his backgrounds are real works of art.  As for the second condition, we
have had Browning, and Meredith is with us.  But there is still much to
be done in the sphere of introspection.  People sometimes say that
fiction is getting too morbid.  As far as psychology is concerned, it has
never been morbid enough.  We have merely touched the surface of the
soul, that is all.  In one single ivory cell of the brain there are
stored away things more marvellous and more terrible than even they have
dreamed of, who, like the author of _Le Rouge et le Noir_, have sought to
track the soul into its most secret places, and to make life confess its
dearest sins.  Still, there is a limit even to the number of untried
backgrounds, and it is possible that a further development of the habit
of introspection may prove fatal to that creative faculty to which it
seeks to supply fresh material.  I myself am inclined to think that
creation is doomed.  It springs from too primitive, too natural an
impulse.  However this may be, it is certain that the subject-matter at
the disposal of creation is always diminishing, while the subject-matter
of criticism increases daily.  There are always new attitudes for the
mind, and new points of view.  The duty of imposing form upon chaos does
not grow less as the world advances.  There was never a time when
Criticism was more needed than it is now.  It is only by its means that
Humanity can become conscious of the point at which it has arrived.--_The
Critic as Artist_.




WITHOUT FRONTIERS


Goethe--you will not misunderstand what I say--was a German of the
Germans.  He loved his country--no man more so.  Its people were dear to
him; and he led them.  Yet, when the iron hoof of Napoleon trampled upon
vineyard and cornfield, his lips were silent.  'How can one write songs
of hatred without hating?' he said to Eckermann, 'and how could I, to
whom culture and barbarism are alone of importance, hate a nation which
is among the most cultivated of the earth and to which I owe so great a
part of my own cultivation?'  This note, sounded in the modern world by
Goethe first, will become, I think, the starting point for the
cosmopolitanism of the future.  Criticism will annihilate
race-prejudices, by insisting upon the unity of the human mind in the
variety of its forms.  If we are tempted to make war upon another nation,
we shall remember that we are seeking to destroy an element of our own
culture, and possibly its most important element.  As long as war is
regarded as wicked, it will always have its fascination.  When it is
looked upon as vulgar, it will cease to be popular.  The change will of
course be slow, and people will not be conscious of it.  They will not
say 'We will not war against France because her prose is perfect,' but
because the prose of France is perfect, they will not hate the land.
Intellectual criticism will bind Europe together in bonds far closer than
those that can be forged by shopman or sentimentalist.  It will give us
the peace that springs from understanding.--_The Critic as Artist_.




THE POETRY OF ARCHAEOLOGY


Infessura tells us that in 1485 some workmen digging on the Appian Way
came across an old Roman sarcophagus inscribed with the name 'Julia,
daughter of Claudius.'  On opening the coffer they found within its
marble womb the body of a beautiful girl of about fifteen years of age,
preserved by the embalmer's skill from corruption and the decay of time.
Her eyes were half open, her hair rippled round her in crisp curling
gold, and from her lips and cheek the bloom of maidenhood had not yet
departed.  Borne back to the Capitol, she became at once the centre of a
new cult, and from all parts of the city crowded pilgrims to worship at
the wonderful shrine, till the Pope, fearing lest those who had found the
secret of beauty in a Pagan tomb might forget what secrets Judaea's rough
and rock-hewn sepulchre contained, had the body conveyed away by night,
and in secret buried.  Legend though it may be, yet the story is none the
less valuable as showing us the attitude of the Renaissance towards the
antique world.  Archaeology to them was not a mere science for the
antiquarian; it was a means by which they could touch the dry dust of
antiquity into the very breath and beauty of life, and fill with the new
wine of romanticism forms that else had been old and outworn.  From the
pulpit of Niccola Pisano down to Mantegna's 'Triumph of Caesar,' and the
service Cellini designed for King Francis, the influence of this spirit
can be traced; nor was it confined merely to the immobile arts--the arts
of arrested movement--but its influence was to be seen also in the great
Graeco-Roman masques which were the constant amusement of the gay courts
of the time, and in the public pomps and processions with which the
citizens of big commercial towns were wont to greet the princes that
chanced to visit them; pageants, by the way, which were considered so
important that large prints were made of them and published--a fact which
is a proof of the general interest at the time in matters of such
kind.--_The Truth of Masks_.




THE ART OF ARCHAEOLOGY


Indeed archaeology is only really delightful when transfused into some
form of art.  I have no desire to underrate the services of laborious
scholars, but I feel that the use Keats made of Lempriere's Dictionary is
of far more value to us than Professor Max Muller's treatment of the same
mythology as a disease of language.  Better _Endymion_ than any theory,
however sound, or, as in the present instance, unsound, of an epidemic
among adjectives!  And who does not feel that the chief glory of
Piranesi's book on Vases is that it gave Keats the suggestion for his
'Ode on a Grecian Urn'?  Art, and art only, can make archaeology
beautiful; and the theatric art can use it most directly and most
vividly, for it can combine in one exquisite presentation the illusion of
actual life with the wonder of the unreal world.  But the sixteenth
century was not merely the age of Vitruvius; it was the age of Vecellio
also.  Every nation seems suddenly to have become interested in the dress
of its neighbours.  Europe began to investigate its own clothes, and the
amount of books published on national costumes is quite extraordinary.  At
the beginning of the century the _Nuremberg Chronicle_, with its two
thousand illustrations, reached its fifth edition, and before the century
was over seventeen editions were published of Munster's _Cosmography_.
Besides these two books there were also the works of Michael Colyns, of
Hans Weigel, of Amman, and of Vecellio himself, all of them well
illustrated, some of the drawings in Vecellio being probably from the
hand of Titian.

Nor was it merely from books and treatises that they acquired their
knowledge.  The development of the habit of foreign travel, the increased
commercial intercourse between countries, and the frequency of diplomatic
missions, gave every nation many opportunities of studying the various
forms of contemporary dress.  After the departure from England, for
instance, of the ambassadors from the Czar, the Sultan and the Prince of
Morocco, Henry the Eighth and his friends gave several masques in the
strange attire of their visitors.  Later on London saw, perhaps too
often, the sombre splendour of the Spanish Court, and to Elizabeth came
envoys from all lands, whose dress, Shakespeare tells us, had an
important influence on English costume.--_The Truth of Masks_.




HEROD SUPPLIANT


Non, non, vous ne voulez pas cela.  Vous me dites cela seulement pour me
faire de la peine, parce que je vous ai regardee pendant toute la soiree.
Eh! bien, oui.  Je vous ai regardee pendant toute la soiree.  Votre
beaute m'a trouble.  Votre beaute m'a terriblement trouble, et je vous ai
trop regardee.  Mais je ne le ferai plus.  Il ne faut regarder ni les
choses ni les personnes.  Il ne faut regarder que dans les miroirs.  Car
les miroirs ne nous montrent que des masques . . . Oh!  Oh! du vin! j'ai
soif . . . Salome, Salome, soyons amis.  Enfin, voyez . . . Qu'est-ce que
je voulais dire?  Qu'est-ce que c'etait?  Ah! je m'en souviens! . . .
Salome!  Non, venez plus pres de moi.  J'ai peur que vous ne m'entendiez
pas . . . Salome, vous connaissez mes paons blancs, mes beaux paons
blancs, qui se promenent dans le jardin entre les myrtes et les grands
cypres.  Leurs becs sont dores, et les grains qu'ils mangent sont dores
aussi, et leurs pieds sont teints de pourpre.  La pluie vient quand ils
crient, et quand ils se pavanent la lune se montre au ciel.  Ils vont
deux a deux entre les cypres et les myrtes noirs et chacun a son esclave
pour le soigner.  Quelquefois ils volent a travers les arbres, et
quelquefois ils couchent sur le gazon et autour de l'etang.  Il n'y a pas
dans le monde d'oiseaux si merveilleux.  Il n'y a aucun roi du monde qui
possede des oiseaux aussi merveilleux.  Je suis sur que meme Cesar ne
possede pas d'oiseaux aussi beaux.  Eh bien! je vous donnerai cinquante
de mes paons.  Ils vous suivront partout, et au milieu d'eux vous serez
comme la lune dans un grand nuage blanc . . . Je vous les donnerai tous.
Je n'en ai que cent, et il n'y a aucun roi du monde qui possede des paons
comme les miens, mais je vous les donnerai tous.  Seulement, il faut me
delier de ma parole et ne pas me demander ce que vous m'avez
demande.--_Salome_.




THE TETRARCH'S REMORSE


Salome, pensez a ce que vous faites.  Cet homme vient peut-etre de Dieu.
Je suis sur qu'il vient de Dieu.  C'est un saint homme.  Le doigt de Dieu
l'a touche.  Dieu a mis dans sa bouche des mots terribles.  Dans le
palais, comme dans le desert, Dieu est toujours avec lui . . . Au moins,
c'est possible.  On ne sait pas, mais il est possible que Dieu soit pour
lui et avec lui.  Aussi peut-etre que s'il mourrait, il m'arriverait un
malheur.  Enfin, il a dit que le jour ou il mourrait il arriverait un
malheur a quelqu'un.  Ce ne peut etre qu'a moi.  Souvenez-vous, j'ai
glisse dans le sang quand je suis entre ici.  Aussi j'ai entendu un
battement d'ailes dans l'air, un battement d'ailes gigantesques.  Ce sont
de tres mauvais presages.  Et il y en avait d'autres.  Je suis sur qu'il
y en avait d'autres, quoique je ne les aie pas vus.  Eh bien!  Salome,
vous ne voulez pas qu'un malheur m'arrive?  Vous ne voulez pas
cela.--_Salome_.




THE TETRARCH'S TREASURE


Moi, je suis tres calme.  Je suis tout a fait calme.  Ecoutez.  J'ai des
bijoux caches ici que meme votre mere n'a jamais vus, des bijoux tout a
fait extraordinaires.  J'ai un collier de perles a quatre rangs.  On
dirait des lunes enchainees de rayons d'argent.  On dirait cinquante
lunes captives dans un filet d'or.  Une reine l'a porte sur l'ivoire de
ses seins.  Toi, quand tu le porteras, tu seras aussi belle qu'une reine.
J'ai des amethystes de deux especes.  Une qui est noire comme le vin.
L'autre qui est rouge comme du vin qu'on a colore avec de l'eau.  J'ai
des topazes jaunes comme les yeux des tigres, et des topazes roses comme
les yeux des pigeons, et des topazes vertes comme les yeux des chats.
J'ai des opales qui brulent toujours avec une flamme qui est tres froide,
des opales qui attristent les esprits et ont peur des tenebres.  J'ai des
onyx semblables aux prunelles d'une morte.  J'ai des selenites qui
changent quand la lune change et deviennent pales quand elles voient le
soleil.  J'ai des saphirs grands comme des oeufs et bleus comme des
fleurs bleues.  La mer erre dedans, et la lune ne vient jamais troubler
le bleu de ses flots.  J'ai des chrysolithes et des beryls, j'ai des
chrysoprases et des rubis, j'ai des sardonyx et des hyacinthes, et des
calcedoines et je vous les donnerai tous, mais tous, et j'ajouterai
d'autres choses.  Le roi des Indes vient justement de m'envoyer quatre
eventails faits de plumes de perroquets, et le roi de Numidie une robe
faite de plumes d'autruche.  J'ai un cristal qu'il n'est pas permis aux
femmes de voir et que meme les jeunes hommes ne doivent regarder qu'apres
avoir ete flagelles de verges.  Dans un coffret de nacre j'ai trois
turquoises merveilleuses.  Quand on les porte sur le front on peut
imaginer des choses qui n'existent pas, et quand on les porte dans la
main on peut rendre les femmes steriles.  Ce sont des tresors de grande
valeur.  Ce sont des tresors sans prix.  Et ce n'est pas tout.  Dans un
coffret d'ebene j'ai deux coupes d'ambre qui ressemblent a des pommes
d'or.  Si un ennemi verse du poison dans ces coupes elles deviennent
comme des pommes d'argent.  Dans un coffret incruste d'ambre j'ai des
sandales incrustees de verre.  J'ai des manteaux qui viennent du pays des
Seres et des bracelets garnis d'escarboucles et de jade qui viennent de
la ville d'Euphrate. . . Enfin, que veux-tu, Salome?  Dis-moi ce que tu
desires et je te le donnerai.  Je te donnerai tout ce que tu demanderas,
sauf une chose.  Je te donnerai tout ce que je possede, sauf une vie.  Je
te donnerai le manteau du grand pretre.  Je te donnerai le voile du
sanctuaire.--_Salome_.




SALOME ANTICIPATES DR. STRAUSS


Ah! tu n'as pas voulu me laisser baiser ta bouche, Iokanaan.  Eh bien! je
la baiserai maintenant.  Je la mordrai avec mes dents comme on mord un
fruit mur.  Oui, je baiserai ta bouche, Iokanaan.  Je te l'ai dit, n'est-
ce pas? je te l'ai dit.  Eh bien! je la baiserai maintenant . . . Mais
pourquoi ne me regardes-tu pas, Iokanaan?  Tes yeux qui etaient si
terribles, qui etaient si pleins de colere et de mepris, ils sont fermes
maintenant.  Pourquoi sont-ils fermes?  Ouvre tes yeux!  Souleve tes
paupieres, Iokanaan.  Pourquoi ne me regardes-tu pas?  As-tu peur de moi,
Iokanaan, que tu ne veux pas me regarder? . . . Et ta langue qui etait
comme un serpent rouge dardant des poisons, elle ne remue plus, elle ne
dit rien maintenant, Iokanaan, cette vipere rouge qui a vomi son venin
sur moi.  C'est etrange, n'est-ce pas?  Comment se fait-il que la vipere
rouge ne remue plus? . . . Tu n'as pas voulu de moi, Iokanaan.  Tu m'as
rejetee.  Tu m'as dit des choses infames.  Tu m'as traitee comme une
courtisane, comme une prostituee, moi, Salome, fille d'Herodias,
Princesse de Judee!  Eh bien, Iokanaan, moi je vis encore, mais toi tu es
mort et ta tete m'appartient.  Je puis en faire ce que je veux.  Je puis
la jeter aux chiens et aux oiseaux de l'air.  Ce que laisseront les
chiens, les oiseaux de l'air le mangeront . . . Ah! Iokanaan, Iokanaan,
tu as ete le seul homme que j'ai aime.  Tous les autres hommes
m'inspirent du degout.  Mais, toi, tu etais beau.  Ton corps etait une
colonne d'ivoire sur un socle d'argent.  C'etait un jardin plein de
colombes et de lis d'argent.  C'etait une tour d'argent ornee de
boucliers d'ivoire.  Il n'y avait rien au monde d'aussi blanc que ton
corps.  Il n'y avait rien au monde d'aussi noir que tes cheveux.  Dans le
monde tout entier il n'y avait rien d'aussi rouge que ta bouche.  Ta voix
etait un encensoir qui repandait d'etranges parfums, et quand je te
regardais j'entendais une musique etrange!  Ah! pourquoi ne m'as-tu pas
regardee, Iokanaan?  Derriere tes mains et tes blasphemes tu as cache ton
visage.  Tu as mis sur tes yeux le bandeau de celui qui veut voir son
Dieu.  Eh bien, tu l'as vu, ton Dieu, Iokanaan, mais moi, moi . . . tu ne
m'as jamais vue.  Si tu m'avais vue, tu m'aurais aimee.  Moi, je t'ai vu,
Iokanaan, et je t'ai aime.  Oh! comme je t'ai aime.  Je t'aime encore,
Iokanaan.  Je n'aime que toi . . . J'ai soif de ta beaute.  J'ai faim de
ton corps.  Et ni le vin, ni les fruits ne peuvent apaiser mon desir.  Que
ferai-je, Iokanaan, maintenant?  Ni les fleuves ni les grandes eaux, ne
pourraient eteindre ma passion.  J'etais une Princesse, tu m'as
dedaignee.  J'etais une vierge, tu m'as defloree.  J'etais chaste, tu as
rempli mes veines de feu . . . Ah!  Ah! pourquoi ne m'as-tu pas regardee,
Iokanaan?  Si tu m'avais regardee tu m'aurais aimee.  Je sais bien que tu
m'aurais aimee, et le mystere de l'amour est plus grand que le mystere de
la mort.  Il ne faut regarder que l'amour.--_Salome_.




THE YOUNG KING


All rare and costly materials had certainly a great fascination for him,
and in his eagerness to procure them he had sent away many merchants,
some to traffic for amber with the rough fisher-folk of the north seas,
some to Egypt to look for that curious green turquoise which is found
only in the tombs of kings, and is said to possess magical properties,
some to Persia for silken carpets and painted pottery, and others to
India to buy gauze and stained ivory, moonstones and bracelets of jade,
sandal-wood and blue enamel and shawls of fine wool.

But what had occupied him most was the robe he was to wear at his
coronation, the robe of tissued gold, and the ruby-studded crown, and the
sceptre with its rows and rings of pearls.  Indeed, it was of this that
he was thinking to-night, as he lay back on his luxurious couch, watching
the great pinewood log that was burning itself out on the open hearth.
The designs, which were from the hands of the most famous artists of the
time, had been submitted to him many months before, and he had given
orders that the artificers were to toil night and day to carry them out,
and that the whole world was to be searched for jewels that would be
worthy of their work.  He saw himself in fancy standing at the high altar
of the cathedral in the fair raiment of a King, and a smile played and
lingered about his boyish lips, and lit up with a bright lustre his dark
woodland eyes.

After some time he rose from his seat, and leaning against the carved
penthouse of the chimney, looked round at the dimly-lit room.  The walls
were hung with rich tapestries representing the Triumph of Beauty.  A
large press, inlaid with agate and lapis-lazuli, filled one corner, and
facing the window stood a curiously wrought cabinet with lacquer panels
of powdered and mosaiced gold, on which were placed some delicate goblets
of Venetian glass, and a cup of dark-veined onyx.  Pale poppies were
broidered on the silk coverlet of the bed, as though they had fallen from
the tired hands of sleep, and tall reeds of fluted ivory bare up the
velvet canopy, from which great tufts of ostrich plumes sprang, like
white foam, to the pallid silver of the fretted ceiling.  A laughing
Narcissus in green bronze held a polished mirror above its head.  On the
table stood a flat bowl of amethyst.

Outside he could see the huge dome of the cathedral, looming like a
bubble over the shadowy houses, and the weary sentinels pacing up and
down on the misty terrace by the river.  Far away, in an orchard, a
nightingale was singing.  A faint perfume of jasmine came through the
open window.  He brushed his brown curls back from his forehead, and
taking up a lute, let his fingers stray across the cords.  His heavy
eyelids drooped, and a strange languor came over him.  Never before had
he felt so keenly, or with such exquisite joy, the magic and the mystery
of beautiful things.

When midnight sounded from the clock-tower he touched a bell, and his
pages entered and disrobed him with much ceremony, pouring rose-water
over his hands, and strewing flowers on his pillow.  A few moments after
that they had left the room, he fell asleep.--_The Young King_.




A CORONATION


And when the Bishop had heard them he knit his brows, and said, 'My son,
I am an old man, and in the winter of my days, and I know that many evil
things are done in the wide world.  The fierce robbers come down from the
mountains, and carry off the little children, and sell them to the Moors.
The lions lie in wait for the caravans, and leap upon the camels.  The
wild boar roots up the corn in the valley, and the foxes gnaw the vines
upon the hill.  The pirates lay waste the sea-coast and burn the ships of
the fishermen, and take their nets from them.  In the salt-marshes live
the lepers; they have houses of wattled reeds, and none may come nigh
them.  The beggars wander through the cities, and eat their food with the
dogs.  Canst thou make these things not to be?  Wilt thou take the leper
for thy bedfellow, and set the beggar at thy board?  Shall the lion do
thy bidding, and the wild boar obey thee?  Is not He who made misery
wiser than thou art?  Wherefore I praise thee not for this that thou hast
done, but I bid thee ride back to the Palace and make thy face glad, and
put on the raiment that beseemeth a king, and with the crown of gold I
will crown thee, and the sceptre of pearl will I place in thy hand.  And
as for thy dreams, think no more of them.  The burden of this world is
too great for one man to bear, and the world's sorrow too heavy for one
heart to suffer.'

'Sayest thou that in this house?' said the young King, and he strode past
the Bishop, and climbed up the steps of the altar, and stood before the
image of Christ.

He stood before the image of Christ, and on his right hand and on his
left were the marvellous vessels of gold, the chalice with the yellow
wine, and the vial with the holy oil.  He knelt before the image of
Christ, and the great candles burned brightly by the jewelled shrine, and
the smoke of the incense curled in thin blue wreaths through the dome.  He
bowed his head in prayer, and the priests in their stiff copes crept away
from the altar.

And suddenly a wild tumult came from the street outside, and in entered
the nobles with drawn swords and nodding plumes, and shields of polished
steel.  'Where is this dreamer of dreams?' they cried.  'Where is this
King who is apparelled like a beggar--this boy who brings shame upon our
state?  Surely we will slay him, for he is unworthy to rule over us.'

And the young King bowed his head again, and prayed, and when he had
finished his prayer he rose up, and turning round he looked at them
sadly.

And lo! through the painted windows came the sunlight streaming upon him,
and the sun-beams wove round him a tissued robe that was fairer than the
robe that had been fashioned for his pleasure.  The dead staff blossomed,
and bare lilies that were whiter than pearls.  The dry thorn blossomed,
and bare roses that were redder than rubies.  Whiter than fine pearls
were the lilies, and their stems were of bright silver.  Redder than male
rubies were the roses, and their leaves were of beaten gold.

He stood there in the raiment of a king, and the gates of the jewelled
shrine flew open, and from the crystal of the many-rayed monstrance shone
a marvellous and mystical light.  He stood there in a king's raiment, and
the Glory of God filled the place, and the saints in their carven niches
seemed to move.  In the fair raiment of a king he stood before them, and
the organ pealed out its music, and the trumpeters blew upon their
trumpets, and the singing boys sang.

And the people fell upon their knees in awe, and the nobles sheathed
their swords and did homage, and the Bishop's face grew pale, and his
hands trembled.  'A greater than I hath crowned thee,' he cried, and he
knelt before him.

And the young King came down from the high altar, and passed home through
the midst of the people.  But no man dared look upon his face, for it was
like the face of an angel.--_The Young King_.




THE KING OF SPAIN


From a window in the palace the sad melancholy King watched them.  Behind
him stood his brother, Don Pedro of Aragon, whom he hated, and his
confessor, the Grand Inquisitor of Granada, sat by his side.  Sadder even
than usual was the King, for as he looked at the Infanta bowing with
childish gravity to the assembling counters, or laughing behind her fan
at the grim Duchess of Albuquerque who always accompanied her, he thought
of the young Queen, her mother, who but a short time before--so it seemed
to him--had come from the gay country of France, and had withered away in
the sombre splendour of the Spanish court, dying just six months after
the birth of her child, and before she had seen the almonds blossom twice
in the orchard, or plucked the second year's fruit from the old gnarled
fig-tree that stood in the centre of the now grass-grown courtyard.  So
great had been his love for her that he had not suffered even the grave
to hide her from him.  She had been embalmed by a Moorish physician, who
in return for this service had been granted his life, which for heresy
and suspicion of magical practices had been already forfeited, men said,
to the Holy Office, and her body was still lying on its tapestried bier
in the black marble chapel of the Palace, just as the monks had borne her
in on that windy March day nearly twelve years before.  Once every month
the King, wrapped in a dark cloak and with a muffled lantern in his hand,
went in and knelt by her side calling out, '_Mi reina_!  _Mi reina_!' and
sometimes breaking through the formal etiquette that in Spain governs
every separate action of life, and sets limits even to the sorrow of a
King, he would clutch at the pale jewelled hands in a wild agony of
grief, and try to wake by his mad kisses the cold painted face.

To-day he seemed to see her again, as he had seen her first at the Castle
of Fontainebleau, when he was but fifteen years of age, and she still
younger.  They had been formally betrothed on that occasion by the Papal
Nuncio in the presence of the French King and all the Court, and he had
returned to the Escurial bearing with him a little ringlet of yellow
hair, and the memory of two childish lips bending down to kiss his hand
as he stepped into his carriage.  Later on had followed the marriage,
hastily performed at Burgos, a small town on the frontier between the two
countries, and the grand public entry into Madrid with the customary
celebration of high mass at the Church of La Atocha, and a more than
usually solemn _auto-da-fe_, in which nearly three hundred heretics,
amongst whom were many Englishmen, had been delivered over to the secular
arm to be burned.

Certainly he had loved her madly, and to the ruin, many thought, of his
country, then at war with England for the possession of the empire of the
New World.  He had hardly ever permitted her to be out of his sight; for
her, he had forgotten, or seemed to have forgotten, all grave affairs of
State; and, with that terrible blindness that passion brings upon its
servants, he had failed to notice that the elaborate ceremonies by which
he sought to please her did but aggravate the strange malady from which
she suffered.  When she died he was, for a time, like one bereft of
reason.  Indeed, there is no doubt but that he would have formally
abdicated and retired to the great Trappist monastery at Granada, of
which he was already titular Prior, had he not been afraid to leave the
little Infanta at the mercy of his brother, whose cruelty, even in Spain,
was notorious, and who was suspected by many of having caused the Queen's
death by means of a pair of poisoned gloves that he had presented to her
on the occasion of her visiting his castle in Aragon.  Even after the
expiration of the three years of public mourning that he had ordained
throughout his whole dominions by royal edict, he would never suffer his
ministers to speak about any new alliance, and when the Emperor himself
sent to him, and offered him the hand of the lovely Archduchess of
Bohemia, his niece, in marriage, he bade the ambassadors tell their
master that the King of Spain was already wedded to Sorrow, and that
though she was but a barren bride he loved her better than Beauty; an
answer that cost his crown the rich provinces of the Netherlands, which
soon after, at the Emperor's instigation, revolted against him under the
leadership of some fanatics of the Reformed Church.--_The Birthday of the
Infranta_.




A BULL FIGHT


A procession of noble boys, fantastically dressed as _toreadors_, came
out to meet her, and the young Count of Tierra-Nueva, a wonderfully
handsome lad of about fourteen years of age, uncovering his head with all
the grace of a born hidalgo and grandee of Spain, led her solemnly in to
a little gilt and ivory chair that was placed on a raised dais above the
arena.  The children grouped themselves all round, fluttering their big
fans and whispering to each other, and Don Pedro and the Grand Inquisitor
stood laughing at the entrance.  Even the Duchess--the Camerera-Mayor as
she was called--a thin, hard-featured woman with a yellow ruff, did not
look quite so bad-tempered as usual, and something like a chill smile
flitted across her wrinkled face and twitched her thin bloodless lips.

It certainly was a marvellous bull-fight, and much nicer, the Infanta
thought, than the real bull-fight that she had been brought to see at
Seville, on the occasion of the visit of the Duke of Parma to her father.
Some of the boys pranced about on richly-caparisoned hobby-horses
brandishing long javelins with gay streamers of bright ribands attached
to them; others went on foot waving their scarlet cloaks before the bull,
and vaulting lightly over the barrier when he charged them; and as for
the bull himself, he was just like a live bull, though he was only made
of wicker-work and stretched hide, and sometimes insisted on running
round the arena on his hind legs, which no live bull ever dreams of
doing.  He made a splendid fight of it too, and the children got so
excited that they stood up upon the benches, and waved their lace
handkerchiefs and cried out: _Bravo toro_!  _Bravo toro_! just as
sensibly as if they had been grown-up people.  At last, however, after a
prolonged combat, during which several of the hobby-horses were gored
through and through, and, their riders dismounted, the young Count of
Tierra-Nueva brought the bull to his knees, and having obtained
permission from the Infanta to give the _coup de grace_, he plunged his
wooden sword into the neck of the animal with such violence that the head
came right off, and disclosed the laughing face of little Monsieur de
Lorraine, the son of the French Ambassador at Madrid.

The arena was then cleared amidst much applause, and the dead
hobby-horses dragged solemnly away by two Moorish pages in yellow and
black liveries, and after a short interlude, during which a French
posture-master performed upon the tightrope, some Italian puppets
appeared in the semi-classical tragedy of _Sophonisba_ on the stage of a
small theatre that had been built up for the purpose.  They acted so
well, and their gestures were so extremely natural, that at the close of
the play the eyes of the Infanta were quite dim with tears.  Indeed some
of the children really cried, and had to be comforted with sweetmeats,
and the Grand Inquisitor himself was so affected that he could not help
saying to Don Pedro that it seemed to him intolerable that things made
simply out of wood and coloured wax, and worked mechanically by wires,
should be so unhappy and meet with such terrible misfortunes.--_The
Birthday of the Infanta_.




THE THRONE ROOM


It was a throne-room, used for the reception of foreign ambassadors, when
the King, which of late had not been often, consented to give them a
personal audience; the same room in which, many years before, envoys had
appeared from England to make arrangements for the marriage of their
Queen, then one of the Catholic sovereigns of Europe, with the Emperor's
eldest son.  The hangings were of gilt Cordovan leather, and a heavy gilt
chandelier with branches for three hundred wax lights hung down from the
black and white ceiling.  Underneath a great canopy of gold cloth, on
which the lions and towers of Castile were broidered in seed pearls,
stood the throne itself, covered with a rich pall of black velvet studded
with silver tulips and elaborately fringed with silver and pearls.  On
the second step of the throne was placed the kneeling-stool of the
Infanta, with its cushion of cloth of silver tissue, and below that
again, and beyond the limit of the canopy, stood the chair for the Papal
Nuncio, who alone had the right to be seated in the King's presence on
the occasion of any public ceremonial, and whose Cardinal's hat, with its
tangled scarlet tassels, lay on a purple _tabouret_ in front.  On the
wall, facing the throne, hung a life-sized portrait of Charles V. in
hunting dress, with a great mastiff by his side, and a picture of Philip
II. receiving the homage of the Netherlands occupied the centre of the
other wall.  Between the windows stood a black ebony cabinet, inlaid with
plates of ivory, on which the figures from Holbein's Dance of Death had
been graved--by the hand, some said, of that famous master himself.

But the little Dwarf cared nothing for all this magnificence.  He would
not have given his rose for all the pearls on the canopy, nor one white
petal of his rose for the throne itself.  What he wanted was to see the
Infanta before she went down to the pavilion, and to ask her to come away
with him when he had finished his dance.  Here, in the Palace, the air
was close and heavy, but in the forest the wind blew free, and the
sunlight with wandering hands of gold moved the tremulous leaves aside.
There were flowers, too, in the forest, not so splendid, perhaps, as the
flowers in the garden, but more sweetly scented for all that; hyacinths
in early spring that flooded with waving purple the cool glens, and
grassy knolls; yellow primroses that nestled in little clumps round the
gnarled roots of the oak-trees; bright celandine, and blue speedwell, and
irises lilac and gold.  There were grey catkins on the hazels, and the
foxgloves drooped with the weight of their dappled bee-haunted cells.  The
chestnut had its spires of white stars, and the hawthorn its pallid moons
of beauty.  Yes: surely she would come if he could only find her!  She
would come with him to the fair forest, and all day long he would dance
for her delight.  A smile lit up his eyes at the thought, and he passed
into the next room.

Of all the rooms this was the brightest and the most beautiful.  The
walls were covered with a pink-flowered Lucca damask, patterned with
birds and dotted with dainty blossoms of silver; the furniture was of
massive silver, festooned with florid wreaths, and swinging Cupids; in
front of the two large fire-places stood great screens broidered with
parrots and peacocks, and the floor, which was of sea-green onyx, seemed
to stretch far away into the distance.  Nor was he alone.  Standing under
the shadow of the doorway, at the extreme end of the room, he saw a
little figure watching him.  His heart trembled, a cry of joy broke from
his lips, and he moved out into the sunlight.  As he did so, the figure
moved out also, and he saw it plainly.--_The Birthday of the Infanta_.




A PROTECTED COUNTRY


'The kings of each city levied tolls on us, but would not suffer us to
enter their gates.  They threw us bread over the walls, little
maize-cakes baked in honey and cakes of fine flour filled with dates.  For
every hundred baskets we gave them a bead of amber.

'When the dwellers in the villages saw us coming, they poisoned the wells
and fled to the hill-summits.  We fought with the Magadae who are born
old, and grow younger and younger every year, and die when they are
little children; and with the Laktroi who say that they are the sons of
tigers, and paint themselves yellow and black; and with the Aurantes who
bury their dead on the tops of trees, and themselves live in dark caverns
lest the Sun, who is their god, should slay them; and with the Krimnians
who worship a crocodile, and give it earrings of green glass, and feed it
with butter and fresh fowls; and with the Agazonbae, who are dog-faced;
and with the Sibans, who have horses' feet, and run more swiftly than
horses.  A third of our company died in battle, and a third died of want.
The rest murmured against me, and said that I had brought them an evil
fortune.  I took a horned adder from beneath a stone and let it sting me.
When they saw that I did not sicken they grew afraid.

'In the fourth month we reached the city of Illel.  It was night-time
when we came to the grove that is outside the walls, and the air was
sultry, for the Moon was travelling in Scorpion.  We took the ripe
pomegranates from the trees, and brake them, and drank their sweet
juices.  Then we lay down on our carpets, and waited for the dawn.

'And at dawn we rose and knocked at the gate of the city.  It was wrought
out of red bronze, and carved with sea-dragons and dragons that have
wings.  The guards looked down from the battlements and asked us our
business.  The interpreter of the caravan answered that we had come from
the island of Syria with much merchandise.  They took hostages, and told
us that they would open the gate to us at noon, and bade us tarry till
then.

'When it was noon they opened the gate, and as we entered in the people
came crowding out of the houses to look at us, and a crier went round the
city crying through a shell.  We stood in the market-place, and the
negroes uncorded the bales of figured cloths and opened the carved chests
of sycamore.  And when they had ended their task, the merchants set forth
their strange wares, the waxed linen from Egypt and the painted linen
from the country of the Ethiops, the purple sponges from Tyre and the
blue hangings from Sidon, the cups of cold amber and the fine vessels of
glass and the curious vessels of burnt clay.  From the roof of a house a
company of women watched us.  One of them wore a mask of gilded leather.

'And on the first day the priests came and bartered with us, and on the
second day came the nobles, and on the third day came the craftsmen and
the slaves.  And this is their custom with all merchants as long as they
tarry in the city.

'And we tarried for a moon, and when the moon was waning, I wearied and
wandered away through the streets of the city and came to the garden of
its god.  The priests in their yellow robes moved silently through the
green trees, and on a pavement of black marble stood the rose-red house
in which the god had his dwelling.  Its doors were of powdered lacquer,
and bulls and peacocks were wrought on them in raised and polished gold.
The tilted roof was of sea-green porcelain, and the jutting eaves were
festooned with little bells.  When the white doves flew past, they struck
the bells with their wings and made them tinkle.

'In front of the temple was a pool of clear water paved with veined onyx.
I lay down beside it, and with my pale fingers I touched the broad
leaves.  One of the priests came towards me and stood behind me.  He had
sandals on his feet, one of soft serpent-skin and the other of birds'
plumage.  On his head was a mitre of black felt decorated with silver
crescents.  Seven yellows were woven into his robe, and his frizzed hair
was stained with antimony.

'After a little while he spake to me, and asked me my desire.

'I told him that my desire was to see the god.'--_The Fisherman and His
Soul_.




THE BLACKMAILING OF THE EMPEROR


'As soon as the man was dead the Emperor turned to me, and when he had
wiped away the bright sweat from his brow with a little napkin of purfled
and purple silk, he said to me, "Art thou a prophet, that I may not harm
thee, or the son of a prophet, that I can do thee no hurt?  I pray thee
leave my city to-night, for while thou art in it I am no longer its
lord."

'And I answered him, "I will go for half of thy treasure.  Give me half
of thy treasure, and I will go away."

'He took me by the hand, and led me out into the garden.  When the
captain of the guard saw me, he wondered.  When the eunuchs saw me, their
knees shook and they fell upon the ground in fear.

'There is a chamber in the palace that has eight walls of red porphyry,
and a brass-sealed ceiling hung with lamps.  The Emperor touched one of
the walls and it opened, and we passed down a corridor that was lit with
many torches.  In niches upon each side stood great wine-jars filled to
the brim with silver pieces.  When we reached the centre of the corridor
the Emperor spake the word that may not be spoken, and a granite door
swung back on a secret spring, and he put his hands before his face lest
his eyes should be dazzled.

'Thou couldst not believe how marvellous a place it was.  There were huge
tortoise-shells full of pearls, and hollowed moonstones of great size
piled up with red rubies.  The gold was stored in coffers of elephant-
hide, and the gold-dust in leather bottles.  There were opals and
sapphires, the former in cups of crystal, and the latter in cups of jade.
Round green emeralds were ranged in order upon thin plates of ivory, and
in one corner were silk bags filled, some with turquoise-stones, and
others with beryls.  The ivory horns were heaped with purple amethysts,
and the horns of brass with chalcedonies and sards.  The pillars, which
were of cedar, were hung with strings of yellow lynx-stones.  In the flat
oval shields there were carbuncles, both wine-coloured and coloured like
grass.  And yet I have told thee but a tithe of what was there.

'And when the Emperor had taken away his hands from before his face he
said to me: "This is my house of treasure, and half that is in it is
thine, even as I promised to thee.  And I will give thee camels and camel
drivers, and they shall do thy bidding and take thy share of the treasure
to whatever part of the world thou desirest to go.  And the thing shall
be done to-night, for I would not that the Sun, who is my father, should
see that there is in my city a man whom I cannot slay."

'But I answered him, "The gold that is here is thine, and the silver also
is thine, and thine are the precious jewels and the things of price.  As
for me, I have no need of these.  Nor shall I take aught from thee but
that little ring that thou wearest on the finger of thy hand."

'And the Emperor frowned.  "It is but a ring of lead," he cried, "nor has
it any value.  Therefore take thy half of the treasure and go from my
city."

'"Nay," I answered, "but I will take nought but that leaden ring, for I
know what is written within it, and for what purpose."

'And the Emperor trembled, and besought me and said, "Take all the
treasure and go from my city.  The half that is mine shall be thine
also."

'And I did a strange thing, but what I did matters not, for in a cave
that is but a day's journey from this place have, I hidden the Ring of
Riches.  It is but a day's journey from this place, and it waits for thy
coming.  He who has this Ring is richer than all the kings of the world.
Come therefore and take it, and the world's riches shall be thine.'--_The
Fisherman and His Soul_.




COVENT GARDEN


Where he went he hardly knew.  He had a dim memory of wandering through a
labyrinth of sordid houses, of being lost in a giant web of sombre
streets, and it was bright dawn when he found himself at last in
Piccadilly Circus.  As he strolled home towards Belgrave Square, he met
the great waggons on their way to Covent Garden.  The white-smocked
carters, with their pleasant sunburnt faces and coarse curly hair, strode
sturdily on, cracking their whips, and calling out now and then to each
other; on the back of a huge grey horse, the leader of a jangling team,
sat a chubby boy, with a bunch of primroses in his battered hat, keeping
tight hold of the mane with his little hands, and laughing; and the great
piles of vegetables looked like masses of jade against the morning sky,
like masses of green jade against the pink petals of some marvellous
rose.  Lord Arthur felt curiously affected, he could not tell why.  There
was something in the dawn's delicate loveliness that seemed to him
inexpressibly pathetic, and he thought of all the days that break in
beauty, and that set in storm.  These rustics, too, with their rough,
good-humoured voices, and their nonchalant ways, what a strange London
they saw!  A London free from the sin of night and the smoke of day, a
pallid, ghost-like city, a desolate town of tombs!  He wondered what they
thought of it, and whether they knew anything of its splendour and its
shame, of its fierce, fiery-coloured joys, and its horrible hunger, of
all it makes and mars from morn to eve.  Probably it was to them merely a
mart where they brought their fruits to sell, and where they tarried for
a few hours at most, leaving the streets still silent, the houses still
asleep.  It gave him pleasure to watch them as they went by.  Rude as
they were, with their heavy, hob-nailed shoes, and their awkward gait,
they brought a little of a ready with them.  He felt that they had lived
with Nature, and that she had taught them peace.  He envied them all that
they did not know.

By the time he had reached Belgrave Square the sky was a faint blue, and
the birds were beginning to twitter in the gardens.--_Lord Arthur
Savile's Crime_.




A LETTER FROM MISS JANE PERCY TO HER AUNT


THE DEANERY, CHICHESTER,

27_th May_.

My Dearest Aunt,

Thank you so much for the flannel for the Dorcas Society, and also for
the gingham.  I quite agree with you that it is nonsense their wanting to
wear pretty things, but everybody is so Radical and irreligious nowadays,
that it is difficult to make them see that they should not try and dress
like the upper classes.  I am sure I don't know what we are coming to.  As
papa has often said in his sermons, we live in an age of unbelief.

We have had great fun over a clock that an unknown admirer sent papa last
Thursday.  It arrived in a wooden box from London, carriage paid, and
papa feels it must have been sent by some one who had read his remarkable
sermon, 'Is Licence Liberty?' for on the top of the clock was a figure of
a woman, with what papa said was the cap of Liberty on her head.  I
didn't think it very becoming myself, but papa said it was historical, so
I suppose it is all right.  Parker unpacked it, and papa put it on the
mantelpiece in the library, and we were all sitting there on Friday
morning, when just as the clock struck twelve, we heard a whirring noise,
a little puff of smoke came from the pedestal of the figure, and the
goddess of Liberty fell off, and broke her nose on the fender!  Maria was
quite alarmed, but it looked so ridiculous, that James and I went off
into fits of laughter, and even papa was amused.  When we examined it, we
found it was a sort of alarum clock, and that, if you set it to a
particular hour, and put some gunpowder and a cap under a little hammer,
it went off whenever you wanted.  Papa said it must not remain in the
library, as it made a noise, so Reggie carried it away to the schoolroom,
and does nothing but have small explosions all day long.  Do you think
Arthur would like one for a wedding present?  I suppose they are quite
fashionable in London.  Papa says they should do a great deal of good, as
they show that Liberty can't last, but must fall down.  Papa says Liberty
was invented at the time of the French Revolution.  How awful it seems!

I have now to go to the Dorcas, where I will read them your most
instructive letter.  How true, dear aunt, your idea is, that in their
rank of life they should wear what is unbecoming.  I must say it is
absurd, their anxiety about dress, when there are so many more important
things in this world, and in the next.  I am so glad your flowered poplin
turned out so well, and that your lace was not torn.  I am wearing my
yellow satin, that you so kindly gave me, at the Bishop's on Wednesday,
and think it will look all right.  Would you have bows or not?  Jennings
says that every one wears bows now, and that the underskirt should be
frilled.  Reggie has just had another explosion, and papa has ordered the
clock to be sent to the stables.  I don't think papa likes it so much as
he did at first, though he is very flattered at being sent such a pretty
and ingenious toy.  It shows that people read his sermons, and profit by
them.

Papa sends his love, in which James, and Reggie, and Maria all unite,
and, hoping that Uncle Cecil's gout is better, believe me, dear aunt,
ever your affectionate niece,

JANE PERCY.

PS.--Do tell me about the bows.  Jennings insists they are the
fashion.--_Lord Arthur Savile's Crime_.




THE TRIUMPH OF AMERICAN 'HUMOR'


At half-past ten he heard the family going to bed.  For some time he was
disturbed by wild shrieks of laughter from the twins, who, with the light-
hearted gaiety of schoolboys, were evidently amusing themselves before
they retired to rest, but at a quarter past eleven all was still, and, as
midnight sounded, he sallied forth.  The owl beat against the window
panes, the raven croaked from the old yew-tree, and the wind wandered
moaning round the house like a lost soul; but the Otis family slept
unconscious of their doom, and high above the rain and storm he could
hear the steady snoring of the Minister for the United States.  He
stepped stealthily out of the wainscoting, with an evil smile on his
cruel, wrinkled mouth, and the moon hid her face in a cloud as he stole
past the great oriel window, where his own arms and those of his murdered
wife were blazoned in azure and gold.  On and on he glided, like an evil
shadow, the very darkness seeming to loathe him as he passed.  Once he
thought he heard something call, and stopped; but it was only the baying
of a dog from the Red Farm, and he went on, muttering strange sixteenth-
century curses, and ever and anon brandishing the rusty dagger in the
midnight air.  Finally he reached the corner of the passage that led to
luckless Washington's room.  For a moment he paused there, the wind
blowing his long grey locks about his head, and twisting into grotesque
and fantastic folds the nameless horror of the dead man's shroud.  Then
the clock struck the quarter, and he felt the time was come.  He chuckled
to himself, and turned the corner; but no sooner had he done so, than,
with a piteous wail of terror, he fell back, and hid his blanched face in
his long, bony hands.  Right in front of him was standing a horrible
spectre, motionless as a carven image, and monstrous as a madman's dream!
Its head was bald and burnished; its face round, and fat, and white; and
hideous laughter seemed to have writhed its features into an eternal
grin.  From the eyes streamed rays of scarlet light, the mouth was a wide
well of fire, and a hideous garment, like to his own, swathed with its
silent snows the Titan form.  On its breast was a placard with strange
writing in antique characters, some scroll of shame it seemed, some
record of wild sins, some awful calendar of crime, and, with its right
hand, it bore aloft a falchion of gleaming steel.

Never having seen a ghost before, he naturally was terribly frightened,
and, after a second hasty glance at the awful phantom, he fled back to
his room, tripping up in his long winding-sheet as he sped down the
corridor, and finally dropping the rusty dagger into the Minister's jack-
boots, where it was found in the morning by the butler.  Once in the
privacy of his own apartment, he flung himself down on a small pallet-
bed, and hid his face under the clothes.  After a time, however, the
brave old Canterville spirit asserted itself, and he determined to go and
speak to the other ghost as soon as it was daylight.  Accordingly, just
as the dawn was touching the hills with silver, he returned towards the
spot where he had first laid eyes on the grisly phantom, feeling that,
after all, two ghosts were better than one, and that, by the aid of his
new friend, he might safely grapple with the twins.  On reaching the
spot, however, a terrible sight met his gaze.  Something had evidently
happened to the spectre, for the light had entirely faded from its hollow
eyes, the gleaming falchion had fallen from its hand, and it was leaning
up against the wall in a strained and uncomfortable attitude.  He rushed
forward and seized it in his arms, when, to his horror, the head slipped
off and rolled on the floor, the body assumed a recumbent posture, and he
found himself clasping a white dimity bed-curtain, with a sweeping-brush,
a kitchen cleaver, and a hollow turnip lying at his feet!--_The
Canterville Ghost_.




THE GARDEN OF DEATH


'Far away beyond the pine-woods,' he answered, in a low dreamy voice,
'there is a little garden.  There the grass grows long and deep, there
are the great white stars of the hemlock flower, there the nightingale
sings all night long.  All night long he sings, and the cold, crystal
moon looks down, and the yew-tree spreads out its giant arms over the
sleepers.'

Virginia's eyes grew dim with tears, and she hid her face in her hands.

'You mean the Garden of Death,' she whispered.

'Yes, Death.  Death must be so beautiful.  To lie in the soft brown
earth, with the grasses waving above one's head, and listen to silence.
To have no yesterday, and no to-morrow.  To forget time, to forgive life,
to be at peace.  You can help me.  You can open for me the portals of
Death's house, for Love is always with you, and Love is stronger than
Death is.'

Virginia trembled, a cold shudder ran through her, and for a few moments
there was silence.  She felt as if she was in a terrible dream.

Then the Ghost spoke again, and his voice sounded like the sighing of the
wind.

'Have you ever read the old prophecy on the library window?'

'Oh, often,' cried the little girl, looking up; 'I know it quite well.  It
is painted in curious black letters, and it is difficult to read.  There
are only six lines:

   When a golden girl can win
   Prayer from out the lips of sin,
   When the barren almond bears,
   And a little child gives away its tears,
   Then shall all the house be still
   And peace come to Canterville.

But I don't know what they mean.'

'They mean,' he said sadly, 'that you must weep for me for my sins,
because I have no tears, and pray with me for my soul, because I have no
faith, and then, if you have always been sweet, and good, and gentle, the
Angel of Death will have mercy on me.  You will see fearful shapes in
darkness, and wicked voices will whisper in your ear, but they will not
harm you, for against the purity of a little child the powers of Hell
cannot prevail.'

Virginia made no answer, and the Ghost wrung his hands in wild despair as
he looked down at her bowed golden head.  Suddenly she stood up, very
pale, and with a strange light in her eyes.  'I am not afraid,' she said
firmly, 'and I will ask the Angel to have mercy on you.'

He rose from his seat with a faint cry of joy, and taking her hand bent
over it with old-fashioned grace and kissed it.  His fingers were as cold
as ice, and his lips burned like fire, but Virginia did not falter, as he
led her across the dusky room.  On the faded green tapestry were
broidered little huntsmen.  They blew their tasselled horns and with
their tiny hands waved to her to go back.  'Go back! little Virginia,'
they cried, 'go back!' but the Ghost clutched her hand more tightly, and
she shut her eyes against them.  Horrible animals with lizard tails, and
goggle eyes, blinked at her from the carven chimney-piece, and murmured
'Beware! little Virginia, beware! we may never see you again,' but the
Ghost glided on more swiftly, and Virginia did not listen.  When they
reached the end of the room he stopped, and muttered some words she could
not understand.  She opened her eyes, and saw the wall slowly fading away
like a mist, and a great black cavern in front of her.  A bitter cold
wind swept round them, and she felt something pulling at her dress.
'Quick, quick,' cried the Ghost, 'or it will be too late,' and, in a
moment, the wainscoting had closed behind them, and the Tapestry Chamber
was empty.--_The Canterville Ghost_.




AN ETON KIT-CAT


"Well," said Erskine, lighting a cigarette, "I must begin by telling you
about Cyril Graham himself.  He and I were at the same house at Eton.  I
was a year or two older than he was, but we were immense friends, and did
all our work and all our play together.  There was, of course, a good
deal more play than work, but I cannot say that I am sorry for that.  It
is always an advantage not to have received a sound commercial education,
and what I learned in the playing fields at Eton has been quite as useful
to me as anything I was taught at Cambridge.  I should tell you that
Cyril's father and mother were both dead.  They had been drowned in a
horrible yachting accident off the Isle of Wight.  His father had been in
the diplomatic service, and had married a daughter, the only daughter, in
fact, of old Lord Crediton, who became Cyril's guardian after the death
of his parents.  I don't think that Lord Crediton cared very much for
Cyril.  He had never really forgiven his daughter for marrying a man who
had not a title.  He was an extraordinary old aristocrat, who swore like
a costermonger, and had the manners of a farmer.  I remember seeing him
once on Speech-day.  He growled at me, gave me a sovereign, and told me
not to grow up 'a damned Radical' like my father.  Cyril had very little
affection for him, and was only too glad to spend most of his holidays
with us in Scotland.  They never really got on together at all.  Cyril
thought him a bear, and he thought Cyril effeminate.  He was effeminate,
I suppose, in some things, though he was a very good rider and a capital
fencer.  In fact he got the foils before he left Eton.  But he was very
languid in his manner, and not a little vain of his good looks, and had a
strong objection to football.  The two things that really gave him
pleasure were poetry and acting.  At Eton he was always dressing up and
reciting Shakespeare, and when he went up to Trinity he became a member
of the A.D.C. his first term.  I remember I was always very jealous of
his acting.  I was absurdly devoted to him; I suppose because we were so
different in some things.  I was a rather awkward, weakly lad, with huge
feet, and horribly freckled.  Freckles run in Scotch families just as
gout does in English families.  Cyril used to say that of the two he
preferred the gout; but he always set an absurdly high value on personal
appearance, and once read a paper before our debating society to prove
that it was better to be good-looking than to be good.  He certainly was
wonderfully handsome.  People who did not like him, Philistines and
college tutors, and young men reading for the Church, used to say that he
was merely pretty; but there was a great deal more in his face than mere
prettiness.  I think he was the most splendid creature I ever saw, and
nothing could exceed the grace of his movements, the charm of his manner.
He fascinated everybody who was worth fascinating, and a great many
people who were not.  He was often wilful and petulant, and I used to
think him dreadfully insincere.  It was due, I think, chiefly to his
inordinate desire to please.  Poor Cyril!  I told him once that he was
contented with very cheap triumphs, but he only laughed.  He was horribly
spoiled.  All charming people, I fancy, are spoiled.  It is the secret of
their attraction.

"However, I must tell you about Cyril's acting.  You know that no
actresses are allowed to play at the A.D.C.  At least they were not in my
time.  I don't know how it is now.  Well, of course, Cyril was always
cast for the girls' parts, and when _As You Like It_ was produced he
played Rosalind.  It was a marvellous performance.  In fact, Cyril Graham
was the only perfect Rosalind I have ever seen.  It would be impossible
to describe to you the beauty, the delicacy, the refinement of the whole
thing.  It made an immense sensation, and the horrid little theatre, as
it was then, was crowded every night.  Even when I read the play now I
can't help thinking of Cyril.  It might have been written for him.  The
next term he took his degree, and came to London to read for the
diplomatic.  But he never did any work.  He spent his days in reading
Shakespeare's Sonnets, and his evenings at the theatre.  He was, of
course, wild to go on the stage.  It was all that I and Lord Crediton
could do to prevent him.  Perhaps if he had gone on the stage he would be
alive now.  It is always a silly thing to give advice, but to give good
advice is absolutely fatal.  I hope you will never fall into that error.
If you do, you will be sorry for it."--_The Portrait of Mr. W. H_.




MRS. ERLYNNE EXERCISES THE PREROGATIVE OF A GRANDMOTHER


Lady Windermere, before Heaven your husband is guiltless of all offence
towards you!  And I--I tell you that had it ever occurred to me that such
a monstrous suspicion would have entered your mind, I would have died
rather than have crossed your life or his--oh! died, gladly died!  Believe
what you choose about me.  I am not worth a moment's sorrow.  But don't
spoil your beautiful young life on my account!  You don't know what may
be in store for you, unless you leave this house at once.  You don't know
what it is to fall into the pit, to be despised, mocked, abandoned,
sneered at--to be an outcast! to find the door shut against one, to have
to creep in by hideous byways, afraid every moment lest the mask should
be stripped from one's face, and all the while to hear the laughter, the
horrible laughter of the world, a thing more tragic than all the tears
the world has ever shed.  You don't know what it is.  One pays for one's
sin, and then one pays again, and all one's life one pays.  You must
never know that.--As for me, if suffering be an expiation, then at this
moment I have expiated all my faults, whatever they have been; for to-
night you have made a heart in one who had it not, made it and broken
it.--But let that pass.  I may have wrecked my own life, but I will not
let you wreck yours.  You--why, you are a mere girl, you would be lost.
You haven't got the kind of brains that enables a woman to get back.  You
have neither the wit nor the courage.  You couldn't stand dishonour!  No!
Go back, Lady Windermere, to the husband who loves you, whom you love.
You have a child, Lady Windermere.  Go back to that child who even now,
in pain or in joy, may be calling to you.  God gave you that child.  He
will require from you that you make his life fine, that you watch over
him.  What answer will you make to God if his life is ruined through you?
Back to your house, Lady Windermere--your husband loves you!  He has
never swerved for a moment from the love he bears you.  But even if he
had a thousand loves, you must stay with your child.  If he was harsh to
you, you must stay with your child.  If he ill-treated you, you must stay
with your child.  If he abandoned you, your place is with your
child.--_Lady Windermere's Fan_.




MOTHERHOOD MORE THAN MARRIAGE


Men don't understand what mothers are.  I am no different from other
women except in the wrong done me and the wrong I did, and my very heavy
punishments and great disgrace.  And yet, to bear you I had to look on
death.  To nurture you I had to wrestle with it.  Death fought with me
for you.  All women have to fight with death to keep their children.
Death, being childless, wants our children from us.  Gerald, when you
were naked I clothed you, when you were hungry I gave you food.  Night
and day all that long winter I tended you.  No office is too mean, no
care too lowly for the thing we women love--and oh! how _I_ loved _you_.
Not Hannah, Samuel more.  And you needed love, for you were weakly, and
only love could have kept you alive.  Only love can keep any one alive.
And boys are careless often and without thinking give pain, and we always
fancy that when they come to man's estate and know us better they will
repay us.  But it is not so.  The world draws them from our side, and
they make friends with whom they are happier than they are with us, and
have amusements from which we are barred, and interests that are not
ours: and they are unjust to us often, for when they find life bitter
they blame us for it, and when they find it sweet we do not taste its
sweetness with them . . . You made many friends and went into their
houses and were glad with them, and I, knowing my secret, did not dare to
follow, but stayed at home and closed the door, shut out the sun and sat
in darkness.  What should I have done in honest households?  My past was
ever with me. . . . And you thought I didn't care for the pleasant things
of life.  I tell you I longed for them, but did not dare to touch them,
feeling I had no right.  You thought I was happier working amongst the
poor.  That was my mission, you imagined.  It was not, but where else was
I to go?  The sick do not ask if the hand that smooths their pillow is
pure, nor the dying care if the lips that touch their brow have known the
kiss of sin.  It was you I thought of all the time; I gave to them the
love you did not need: lavished on them a love that was not theirs . . .
And you thought I spent too much of my time in going to Church, and in
Church duties.  But where else could I turn?  God's house is the only
house where sinners are made welcome, and you were always in my heart,
Gerald, too much in my heart.  For, though day after day, at morn or
evensong, I have knelt in God's house, I have never repented of my sin.
How could I repent of my sin when you, my love, were its fruit!  Even now
that you are bitter to me I cannot repent.  I do not.  You are more to me
than innocence.  I would rather be your mother--oh! much rather!--than
have been always pure . . . Oh, don't you see? don't you understand?  It
is my dishonour that has made you so dear to me.  It is my disgrace that
has bound you so closely to me.  It is the price I paid for you--the
price of soul and body--that makes me love you as I do.  Oh, don't ask me
to do this horrible thing.  Child of my shame, be still the child of my
shame!--_A Woman of No Importance_.




THE DAMNABLE IDEAL


Why can't you women love us, faults and all?  Why do you place us on
monstrous pedestals?  We have all feet of clay, women as well as men; but
when we men love women, we love them knowing their weaknesses, their
follies, their imperfections, love them all the more, it may be, for that
reason.  It is not the perfect, but the imperfect, who have need of love.
It is when we are wounded by our own hands, or by the hands of others,
that love should come to cure us--else what use is love at all?  All
sins, except a sin against itself, Love should forgive.  All lives, save
loveless lives, true Love should pardon.  A man's love is like that.  It
is wider, larger, more human than a woman's.  Women think that they are
making ideals of men.  What they are making of us are false idols merely.
You made your false idol of me, and I had not the courage to come down,
show you my wounds, tell you my weaknesses.  I was afraid that I might
lose your love, as I have lost it now.  And so, last night you ruined my
life for me--yes, ruined it!  What this woman asked of me was nothing
compared to what she offered to me.  She offered security, peace,
stability.  The sin of my youth, that I had thought was buried, rose up
in front of me, hideous, horrible, with its hands at my throat.  I could
have killed it for ever, sent it back into its tomb, destroyed its
record, burned the one witness against me.  You prevented me.  No one but
you, you know it.  And now what is there before me but public disgrace,
ruin, terrible shame, the mockery of the world, a lonely dishonoured
life, a lonely dishonoured death, it may be, some day?  Let women make no
more ideals of men! let them not put them on alters and bow before them,
or they may ruin other lives as completely as you--you whom I have so
wildly loved--have ruined mine!--_An Ideal Husband_.




FROM A REJECTED PRIZE-ESSAY


Nations may not have missions but they certainly have functions.  And the
function of ancient Italy was not merely to give us what is statical in
our institutions and rational in our law, but to blend into one elemental
creed the spiritual aspirations of Aryan and of Semite.  Italy was not a
pioneer in intellectual progress, nor a motive power in the evolution of
thought.  The owl of the goddess of Wisdom traversed over the whole land
and found nowhere a resting-place.  The dove, which is the bird of
Christ, flew straight to the city of Rome and the new reign began.  It
was the fashion of early Italian painters to represent in mediaeval
costume the soldiers who watched over the tomb of Christ, and this, which
was the result of the frank anachronism of all true art, may serve to us
as an allegory.  For it was in vain that the Middle Ages strove to guard
the buried spirit of progress.  When the dawn of the Greek spirit arose,
the sepulchre was empty, the grave-clothes laid aside.  Humanity had
risen from the dead.

The study of Greek, it has been well said, implies the birth of
criticism, comparison and research.  At the opening of that education of
modern by ancient thought which we call the Renaissance, it was the words
of Aristotle which sent Columbus sailing to the New World, while a
fragment of Pythagorean astronomy set Copernicus thinking on that train
of reasoning which has revolutionised the whole position of our planet in
the universe.  Then it was seen that the only meaning of progress is a
return to Greek modes of thought.  The monkish hymns which obscured the
pages of Greek manuscripts were blotted out, the splendours of a new
method were unfolded to the world, and out of the melancholy sea of
mediaevalism rose the free spirit of man in all that splendour of glad
adolescence, when the bodily powers seem quickened by a new vitality,
when the eye sees more clearly than its wont and the mind apprehends what
was beforetime hidden from it.  To herald the opening of the sixteenth
century, from the little Venetian printing press came forth all the great
authors of antiquity, each bearing on the title-page the words [Greek
text]; words which may serve to remind us with what wondrous prescience
Polybius saw the world's fate when he foretold the material sovereignty
of Roman institutions and exemplified in himself the intellectual empire
of Greece.

The course of the study of the spirit of historical criticism has not
been a profitless investigation into modes and forms of thought now
antiquated and of no account.  The only spirit which is entirely removed
from us is the mediaeval; the Greek spirit is essentially modern.  The
introduction of the comparative method of research which has forced
history to disclose its secrets belongs in a measure to us.  Ours, too,
is a more scientific knowledge of philology and the method of survival.
Nor did the ancients know anything of the doctrine of averages or of
crucial instances, both of which methods have proved of such importance
in modern criticism, the one adding a most important proof of the
statical elements of history, and exemplifying the influences of all
physical surroundings on the life of man; the other, as in the single
instance of the Moulin Quignon skull, serving to create a whole new
science of prehistoric archaeology and to bring us back to a time when
man was coeval with the stone age, the mammoth and the woolly rhinoceros.
But, except these, we have added no new canon or method to the science of
historical criticism.  Across the drear waste of a thousand years the
Greek and the modern spirit join hands.

In the torch race which the Greek boys ran from the Cerameician field of
death to the home of the goddess of Wisdom, not merely he who first
reached the goal but he also who first started with the torch aflame
received a prize.  In the Lampadephoria of civilisation and free thought
let us not forget to render due meed of honour to those who first lit
that sacred flame, the increasing splendour of which lights our footsteps
to the far-off divine event of the attainment of perfect truth.--_The
Rise of Historical Criticism_.




THE POSSIBILITIES OF THE USEFUL


There are two kinds of men in the world, two great creeds, two different
forms of natures: men to whom the end of life is action, and men to whom
the end of life is thought.  As regards the latter, who seek for
experience itself and not for the fruits of experience, who must burn
always with one of the passions of this fiery-coloured world, who find
life interesting not for its secret but for its situations, for its
pulsations and not for its purpose; the passion for beauty engendered by
the decorative arts will be to them more satisfying than any political or
religious enthusiasm, any enthusiasm for humanity, any ecstasy or sorrow
for love.  For art comes to one professing primarily to give nothing but
the highest quality to one's moments, and for those moments' sake.  So
far for those to whom the end of life is thought.  As regards the others,
who hold that life is inseparable from labour, to them should this
movement be specially dear: for, if our days are barren without industry,
industry without art is barbarism.

Hewers of wood and drawers of water there must be always indeed among us.
Our modern machinery has not much lightened the labour of man after all:
but at least let the pitcher that stands by the well be beautiful and
surely the labour of the day will be lightened: let the wood be made
receptive of some lovely form, some gracious design, and there will come
no longer discontent but joy to the toiler.  For what is decoration but
the worker's expression of joy in his work?  And not joy merely--that is
a great thing yet not enough--but that opportunity of expressing his own
individuality which, as it is the essence of all life, is the source of
all art.  'I have tried,' I remember William Morris saying to me once, 'I
have tried to make each of my workers an artist, and when I say an artist
I mean a man.'  For the worker then, handicraftsman of whatever kind he
is, art is no longer to be a purple robe woven by a slave and thrown over
the whitened body of a leprous king to hide and to adorn the sin of his
luxury, but rather the beautiful and noble expression of a life that has
in it something beautiful and noble.--_The English Renaissance of Art_.




THE ARTIST


ONE evening there came into his soul the desire to fashion an image of
_The Pleasure that abideth for a Moment_.  And he went forth into the
world to look for bronze.  For he could think only in bronze.

But all the bronze of the whole world had disappeared, nor anywhere in
the whole world was there any bronze to be found, save only the bronze of
the image of _The Sorrow that endureth for Ever_.

Now this image he had himself, and with his own hands, fashioned, and had
set it on the tomb of the one thing he had loved in life.  On the tomb of
the dead thing he had most loved had he set this image of his own
fashioning, that it might serve as a sign of the love of man that dieth
not, and a symbol of the sorrow of man that endureth for ever.  And in
the whole world there was no other bronze save the bronze of this image.

And he took the image he had fashioned, and set it in a great furnace,
and gave it to the fire.

And out of the bronze of the image of _The Sorrow that endureth for Ever_
he fashioned an image of _The Pleasure that abideth for a Moment_.--_Poems
in Prose_.




THE DOER OF GOOD


It was night-time and He was alone.

And He saw afar-off the walls of a round city and went towards the city.

And when He came near He heard within the city the tread of the feet of
joy, and the laughter of the mouth of gladness and the loud noise of many
lutes.  And He knocked at the gate and certain of the gate-keepers opened
to Him.

And He beheld a house that was of marble and had fair pillars of marble
before it.  The pillars were hung with garlands, and within and without
there were torches of cedar.  And He entered the house.

And when He had passed through the hall of chalcedony and the hall of
jasper, and reached the long hall of feasting, He saw lying on a couch of
sea-purple one whose hair was crowned with red roses and whose lips were
red with wine.

And He went behind him and touched him on the shoulder and said to him,
'Why do you live like this?'

And the young man turned round and recognised Him, and made answer and
said, 'But I was a leper once, and you healed me.  How else should I
live?'

And He passed out of the house and went again into the street.

And after a little while He saw one whose face and raiment were painted
and whose feet were shod with pearls.  And behind her came, slowly as a
hunter, a young man who wore a cloak of two colours.  Now the face of the
woman was as the fair face of an idol, and the eyes of the young man were
bright with lust.

And He followed swiftly and touched the hand of the young man and said to
him, 'Why do you look at this woman and in such wise?'

And the young man turned round and recognised Him and said, 'But I was
blind once, and you gave me sight.  At what else should I look?'

And He ran forward and touched the painted raiment of the woman and said
to her, 'Is there no other way in which to walk save the way of sin?'

And the woman turned round and recognised Him, and laughed and said, 'But
you forgave me my sins, and the way is a pleasant way.'

And He passed out of the city.

And when He had passed out of the city He saw seated by the roadside a
young man who was weeping.

And He went towards him and touched the long locks of his hair and said
to him, 'Why are you weeping?'

And the young man looked up and recognised Him and made answer, 'But I
was dead once, and you raised me from the dead.  What else should I do
but weep?'--_Poems in Prose_.




THE DISCIPLE


When Narcissus died the pool of his pleasure changed from a cup of sweet
waters into a cup of salt tears, and the Oreads came weeping through the
woodland that they might sing to the pool and give it comfort.

And when they saw that the pool had changed from a cup of sweet waters
into a cup of salt tears, they loosened the green tresses of their hair
and cried to the pool and said, 'We do not wonder that you should mourn
in this manner for Narcissus, so beautiful was he.'

'But was Narcissus beautiful?' said the pool.

'Who should know that better than you?' answered the Oreads.  'Us did he
ever pass by, but you he sought for, and would lie on your banks and look
down at you, and in the mirror of your waters he would mirror his own
beauty.'

And the pool answered, 'But I loved Narcissus because, as he lay on my
banks and looked down at me, in the mirror of his eyes I saw ever my own
beauty mirrored.'--_Poems in Prose_.




THE MASTER


Now when the darkness came over the earth Joseph of Arimathea, having
lighted a torch of pinewood, passed down from the hill into the valley.
For he had business in his own home.

And kneeling on the flint stones of the Valley of Desolation he saw a
young man who was naked and weeping.  His hair was the colour of honey,
and his body was as a white flower, but he had wounded his body with
thorns and on his hair had he set ashes as a crown.

And he who had great possessions said to the young man who was naked and
weeping, 'I do not wonder that your sorrow is so great, for surely He was
a just man.'

And the young man answered, 'It is not for Him that I am weeping, but for
myself.  I too have changed water into wine, and I have healed the leper
and given sight to the blind.  I have walked upon the waters, and from
the dwellers in the tombs I have cast out devils.  I have fed the hungry
in the desert where there was no food, and I have raised the dead from
their narrow houses, and at my bidding, and before a great multitude, of
people, a barren fig-tree withered away.  All things that this man has
done I have done also.  And yet they have not crucified me.'--_Poems in
Prose_.




THE HOUSE OF JUDGMENT


And there was silence in the House of Judgment, and the Man came naked
before God.

And God opened the Book of the Life of the Man.

And God said to the Man, 'Thy life hath been evil, and thou hast shown
cruelty to those who were in need of succour, and to those who lacked
help thou hast been bitter and hard of heart.  The poor called to thee
and thou didst not hearken, and thine ears were closed to the cry of My
afflicted.  The inheritance of the fatherless thou didst take unto
thyself, and thou didst send the foxes into the vineyard of thy
neighbour's field.  Thou didst take the bread of the children and give it
to the dogs to eat, and My lepers who lived in the marshes, and were at
peace and praised Me, thou didst drive forth on to the highways, and on
Mine earth out of which I made thee thou didst spill innocent blood.'

And the Man made answer and said, 'Even so did I.'

And again God opened the Book of the Life of the Man.

And God said to the Man, 'Thy life hath been evil, and the Beauty I have
shown thou hast sought for, and the Good I have hidden thou didst pass
by.  The walls of thy chamber were painted with images, and from the bed
of thine abominations thou didst rise up to the sound of flutes.  Thou
didst build seven altars to the sins I have suffered, and didst eat of
the thing that may not be eaten, and the purple of thy raiment was
broidered with the three signs of shame.  Thine idols were neither of
gold nor of silver that endure, but of flesh that dieth.  Thou didst
stain their hair with perfumes and put pomegranates in their hands.  Thou
didst stain their feet with saffron and spread carpets before them.  With
antimony thou didst stain their eyelids and their bodies thou didst smear
with myrrh.  Thou didst bow thyself to the ground before them, and the
thrones of thine idols were set in the sun.  Thou didst show to the sun
thy shame and to the moon thy madness.'

And the Man made answer and said, 'Even so did I.'

And a third time God opened the Book of the Life of the Man.

And God said to the Man, 'Evil hath been thy life, and with evil didst
thou requite good, and with wrongdoing kindness.  The hands that fed thee
thou didst wound, and the breasts that gave thee suck thou didst despise.
He who came to thee with water went away thirsting, and the outlawed men
who hid thee in their tents at night thou didst betray before dawn.  Thine
enemy who spared thee thou didst snare in an ambush, and the friend who
walked with thee thou didst sell for a price, and to those who brought
thee Love thou didst ever give Lust in thy turn.'

And the Man made answer and said, 'Even so did I.'

And God closed the Book of the Life of the Man, and said, 'Surely I will
send thee into Hell.  Even into Hell will I send thee.'

And the Man cried out, 'Thou canst not.'

And God said to the Man, 'Wherefore can I not send thee to Hell, and for
what reason?'

'Because in Hell have I always lived,' answered the Man.

And there was silence in the House of Judgment.

And after a space God spake, and said to the Man, 'Seeing that I may not
send thee into Hell, surely I will send thee unto Heaven.  Even unto
Heaven will I send thee.'

And the Man cried out, 'Thou canst not.'

And God said to the Man, 'Wherefore can I not send thee unto Heaven, and
for what reason?'

'Because never, and in no place, have I been able to imagine it,'
answered the Man.

And there was silence in the House of Judgment.--_Poems in Prose_.




THE TEACHER OF WISDOM


From his childhood he had been as one filled with the perfect knowledge
of God, and even while he was yet but a lad many of the saints, as well
as certain holy women who dwelt in the free city of his birth, had been
stirred to much wonder by the grave wisdom of his answers.

And when his parents had given him the robe and the ring of manhood he
kissed them, and left them and went out into the world, that he might
speak to the world about God.  For there were at that time many in the
world who either knew not God at all, or had but an incomplete knowledge
of Him, or worshipped the false gods who dwell in groves and have no care
of their worshippers.

And he set his face to the sun and journeyed, walking without sandals, as
he had seen the saints walk, and carrying at his girdle a leathern wallet
and a little water-bottle of burnt clay.

And as he walked along the highway he was full of the joy that comes from
the perfect knowledge of God, and he sang praises unto God without
ceasing; and after a time he reached a strange land in which there were
many cities.

And he passed through eleven cities.  And some of these cities were in
valleys, and others were by the banks of great rivers, and others were
set on hills.  And in each city he found a disciple who loved him and
followed him, and a great multitude also of people followed him from each
city, and the knowledge of God spread in the whole land, and many of the
rulers were converted, and the priests of the temples in which there were
idols found that half of their gain was gone, and when they beat upon
their drums at noon none, or but a few, came with peacocks and with
offerings of flesh as had been the custom of the land before his coming.

Yet the more the people followed him, and the greater the number of his
disciples, the greater became his sorrow.  And he knew not why his sorrow
was so great.  For he spake ever about God, and out of the fulness of
that perfect knowledge of God which God had Himself given to him.

And one evening he passed out of the eleventh city, which was a city of
Armenia, and his disciples and a great crowd of people followed after
him; and he went up on to a mountain and sat down on a rock that was on
the mountain, and his disciples stood round him, and the multitude knelt
in the valley.

And he bowed his head on his hands and wept, and said to his Soul, 'Why
is it that I am full of sorrow and fear, and that each of my disciples is
an enemy that walks in the noonday?'  And his Soul answered him and said,
'God filled thee with the perfect knowledge of Himself, and thou hast
given this knowledge away to others.  The pearl of great price thou hast
divided, and the vesture without seam thou hast parted asunder.  He who
giveth away wisdom robbeth himself.  He is as one who giveth his treasure
to a robber.  Is not God wiser than thou art?  Who art thou to give away
the secret that God hath told thee?  I was rich once, and thou hast made
me poor.  Once I saw God, and now thou hast hidden Him from me.'

And he wept again, for he knew that his Soul spake truth to him, and that
he had given to others the perfect knowledge of God, and that he was as
one clinging to the skirts of God, and that his faith was leaving him by
reason of the number of those who believed in him.

And he said to himself, 'I will talk no more about God.  He who giveth
away wisdom robbeth himself.'

And after the space of some hours his disciples came near him and bowed
themselves to the ground and said, 'Master, talk to us about God, for
thou hast the perfect knowledge of God, and no man save thee hath this
knowledge.'

And he answered them and said, 'I will talk to you about all other things
that are in heaven and on earth, but about God I will not talk to you.
Neither now, nor at any time, will I talk to you about God.'

And they were wroth with him and said to him, 'Thou hast led us into the
desert that we might hearken to thee.  Wilt thou send us away hungry, and
the great multitude that thou hast made to follow thee?'

And he answered them and said, 'I will not talk to you about God.'

And the multitude murmured against him and said to him, 'Thou hast led us
into the desert, and hast given us no food to eat.  Talk to us about God
and it will suffice us.'

But he answered them not a word.  For he knew that if he spake to them
about God he would give away his treasure.

And his disciples went away sadly, and the multitude of people returned
to their own homes.  And many died on the way.

And when he was alone he rose up and set his face to the moon, and
journeyed for seven moons, speaking to no man nor making any answer.  And
when the seventh moon had waned he reached that desert which is the
desert of the Great River.  And having found a cavern in which a Centaur
had once dwelt, he took it for his place of dwelling, and made himself a
mat of reeds on which to lie, and became a hermit.  And every hour the
Hermit praised God that He had suffered him to keep some knowledge of Him
and of His wonderful greatness.

Now, one evening, as the Hermit was seated before the cavern in which he
had made his place of dwelling, he beheld a young man of evil and
beautiful face who passed by in mean apparel and with empty hands.  Every
evening with empty hands the young man passed by, and every morning he
returned with his hands full of purple and pearls.  For he was a Robber
and robbed the caravans of the merchants.

And the Hermit looked at him and pitied him.  But he spake not a word.
For he knew that he who speaks a word loses his faith.

And one morning, as the young man returned with his hands full of purple
and pearls, he stopped and frowned and stamped his foot upon the sand,
and said to the Hermit: 'Why do you look at me ever in this manner as I
pass by?  What is it that I see in your eyes?  For no man has looked at
me before in this manner.  And the thing is a thorn and a trouble to me.'

And the Hermit answered him and said, 'What you see in my eyes is pity.
Pity is what looks out at you from my eyes.'

And the young man laughed with scorn, and cried to the Hermit in a bitter
voice, and said to him, 'I have purple and pearls in my hands, and you
have but a mat of reeds on which to lie.  What pity should you have for
me?  And for what reason have you this pity?'

'I have pity for you,' said the Hermit, 'because you have no knowledge of
God.'

'Is this knowledge of God a precious thing?' asked the young man, and he
came close to the mouth of the cavern.

'It is more precious than all the purple and the pearls of the world,'
answered the Hermit.

'And have you got it?' said the young Robber, and he came closer still.

'Once, indeed,' answered the Hermit, 'I possessed the perfect knowledge
of God.  But in my foolishness I parted with it, and divided it amongst
others.  Yet even now is such knowledge as remains to me more precious
than purple or pearls.'

And when the young Robber heard this he threw away the purple and the
pearls that he was bearing in his hands, and drawing a sharp sword of
curved steel he said to the Hermit, 'Give me, forthwith this knowledge of
God that you possess, or I will surely slay you.  Wherefore should I not
slay him who has a treasure greater than my treasure?'

And the Hermit spread out his arms and said, 'Were it not better for me
to go unto the uttermost courts of God and praise Him, than to live in
the world and have no knowledge of Him?  Slay me if that be your desire.
But I will not give away my knowledge of God.'

And the young Robber knelt down and besought him, but the Hermit would
not talk to him about God, nor give him his Treasure, and the young
Robber rose up and said to the Hermit, 'Be it as you will.  As for
myself, I will go to the City of the Seven Sins, that is but three days'
journey from this place, and for my purple they will give me pleasure,
and for my pearls they will sell me joy.'  And he took up the purple and
the pearls and went swiftly away.

And the Hermit cried out and followed him and besought him.  For the
space of three days he followed the young Robber on the road and
entreated him to return, nor to enter into the City of the Seven Sins.

And ever and anon the young Robber looked back at the Hermit and called
to him, and said, 'Will you give me this knowledge of God which is more
precious than purple and pearls?  If you will give me that, I will not
enter the city.'

And ever did the Hermit answer, 'All things that I have I will give thee,
save that one thing only.  For that thing it is not lawful for me to give
away.'

And in the twilight of the third day they came nigh to the great scarlet
gates of the City of the Seven Sins.  And from the city there came the
sound of much laughter.

And the young Robber laughed in answer, and sought to knock at the gate.
And as he did so the Hermit ran forward and caught him by the skirts of
his raiment, and said to him: 'Stretch forth your hands, and set your
arms around my neck, and put your ear close to my lips, and I will give
you what remains to me of the knowledge of God.'  And the young Robber
stopped.

And when the Hermit had given away his knowledge of God, he fell upon the
ground and wept, and a great darkness hid from him the city and the young
Robber, so that he saw them no more.

And as he lay there weeping he was ware of One who was standing beside
him; and He who was standing beside him had feet of brass and hair like
fine wool.  And He raised the Hermit up, and said to him: 'Before this
time thou hadst the perfect knowledge of God.  Now thou shalt have the
perfect love of God.  Wherefore art thou weeping?'  And he kissed
him.--_Poems in Prose_.




WILDE GIVES DIRECTIONS ABOUT 'DE PROFUNDIS'


H.M. PRISON, READING.

April 1st, 1897.

My Dear Robbie,--I send you a MS. separate from this, which I hope will
arrive safely.  As soon as you have read it, I want you to have it
carefully copied for me.  There are many causes why I wish this to be
done.  One will suffice.  I want you to be my literary executor in case
of my death, and to have complete control of my plays, books, and papers.
As soon as I find I have a legal right to make a will, I will do so.  My
wife does not understand my art, nor could be expected to have any
interest in it, and Cyril is only a child.  So I turn naturally to you,
as indeed I do for everything, and would like you to have all my works.
The deficit that their sale will produce may be lodged to the credit of
Cyril and Vivian.  Well, if you are my literary executor, you must be in
possession of the only document that gives any explanation of my
extraordinary behaviour . . . When you have read the letter, you will see
the psychological explanation of a course of conduct that from the
outside seems a combination of absolute idiotcy with vulgar bravado.  Some
day the truth will have to be known--not necessarily in my lifetime . . .
but I am not prepared to sit in the grotesque pillory they put me into,
for all time; for the simple reason that I inherited from my father and
mother a name of high distinction in literature and art, and I cannot for
eternity allow that name to be degraded.  I don't defend my conduct.  I
explain it.  Also there are in my letter certain passages which deal with
my mental development in prison, and the inevitable evolution of my
character and intellectual attitude towards life that has taken place:
and I want you and others who still stand by me and have affection for me
to know exactly in what mood and manner I hope to face the world.  Of
course from one point of view I know that on the day of my release I
shall be merely passing from one prison into another, and there are times
when the whole world seems to me no larger than my cell and as full of
terror for me.  Still I believe that at the beginning God made a world
for each separate man, and in that world which is within us we should
seek to live.  At any rate you will read those parts of my letter with
less pain than the others.  Of course I need not remind you how fluid a
thing thought is with me--with us all--and of what an evanescent
substance are our emotions made.  Still I do see a sort of possible goal
towards which, through art, I may progress.  It is not unlikely that you
may help me.

As regards the mode of copying: of course it is too long for any
amanuensis to attempt: and your own handwriting, dear Robbie, in your
last letter seems specially designed to remind me that the task is not to
be yours.  I think that the only thing to do is to be thoroughly modern
and to have it typewritten.  Of course the MS. should not pass out of
your control, but could you not get Mrs. Marshall to send down one of her
type-writing girls--women are the most reliable as they have no memory
for the important--to Hornton Street or Phillimore Gardens, to do it
under your supervision?  I assure you that the typewriting machine, when
played with expression, is not more annoying than the piano when played
by a sister or near relation.  Indeed many among those most devoted to
domesticity prefer it.  I wish the copy to be done not on tissue paper
but on good paper such as is used for plays, and a wide rubricated margin
should be left for corrections . . . If the copy is done at Hornton
Street the lady typewriter might be fed through a lattice in the door,
like the Cardinals when they elect a Pope; till she comes out on the
balcony and can say to the world: "Habet Mundus Epistolam"; for indeed it
is an Encyclical letter, and as the Bulls of the Holy Father are named
from their opening words, it may be spoken of as the "_Epistola_: _in
Carcere et Vinculis_." . . . In point of fact, Robbie, prison life makes
one see people and things as they really are.  That is why it turns one
to stone.  It is the people outside who are deceived by the illusions of
a life in constant motion.  They revolve with life and contribute to its
unreality.  We who are immobile both see and know.  Whether or not the
letter does good to narrow natures and hectic brains, to me it has done
good.  I have "cleansed my bosom of much perilous stuff"; to borrow a
phrase from the poet whom you and I once thought of rescuing from the
Philistines.  I need not remind you that mere expression is to an artist
the supreme and only mode of life.  It is by utterance that we live.  Of
the many, many things for which I have to thank the Governor there is
none for which I am more grateful than for his permission to write fully
and at as great a length as I desire.  For nearly two years I had within
a growing burden of bitterness, of much of which I have now got rid.  On
the other side of the prison wall there are some poor black
soot-besmirched trees that are just breaking out into buds of an almost
shrill green.  I know quite well what they are going through.  They are
finding expression.

Ever yours,

OSCAR.

--_Letter from Reading Prison to Robert Ross_.




CAREY STREET


Where there is sorrow there in holy ground.  Some day people will realise
what that means.  They will know nothing of life till they do,--and
natures like his can realise it.  When I was brought down from my prison
to the Court of Bankruptcy, between two policemen,--waited in the long
dreary corridor that, before the whole crowd, whom an action so sweet and
simple hushed into silence, he might gravely raise his hat to me, as,
handcuffed and with bowed head, I passed him by.  Men have gone to heaven
for smaller things than that.  It was in this spirit, and with this mode
of love, that the saints knelt down to wash the feet of the poor, or
stooped to kiss the leper on the cheek.  I have never said one single
word to him about what he did.  I do not know to the present moment
whether he is aware that I was even conscious of his action.  It is not a
thing for which one can render formal thanks in formal words.  I store it
in the treasure-house of my heart.  I keep it there as a secret debt that
I am glad to think I can never possibly repay.  It is embalmed and kept
sweet by the myrrh and cassia of many tears.  When wisdom has been
profitless to me, philosophy barren, and the proverbs and phrases of
those who have sought to give me consolation as dust and ashes in my
mouth, the memory of that little, lovely, silent act of love has unsealed
for me all the wells of pity: made the desert blossom like a rose, and
brought me out of the bitterness of lonely exile into harmony with the
wounded, broken, and great heart of the world.  When people are able to
understand, not merely how beautiful ---'s action was, but why it meant
so much to me, and always will mean so much, then, perhaps, they will
realise how and in what spirit they should approach me. . . .

The poor are wise, more charitable, more kind, more sensitive than we
are.  In their eyes prison is a tragedy in a man's life, a misfortune, a
casuality, something that calls for sympathy in others.  They speak of
one who is in prison as of one who is 'in trouble' simply.  It is the
phrase they always use, and the expression has the perfect wisdom of love
in it.  With people of our own rank it is different.  With us, prison
makes a man a pariah.  I, and such as I am, have hardly any right to air
and sun.  Our presence taints the pleasures of others.  We are unwelcome
when we reappear.  To revisit the glimpses of the moon is not for us.  Our
very children are taken away.  Those lovely links with humanity are
broken.  We are doomed to be solitary, while our sons still live.  We are
denied the one thing that might heal us and keep us, that might bring
balm to the bruised heart, and peace to the soul in pain.--_De
Profundis_.




SORROW WEARS NO MASK


Sorrow, being the supreme emotion of which man is capable, is at once the
type and test of all great art.  What the artist is always looking for is
the mode of existence in which soul and body are one and indivisible: in
which the outward is expressive of the inward: in which form reveals.  Of
such modes of existence there are not a few: youth and the arts
preoccupied with youth may serve as a model for us at one moment: at
another we may like to think that, in its subtlety and sensitiveness of
impression, its suggestion of a spirit dwelling in external things and
making its raiment of earth and air, of mist and city alike, and in its
morbid sympathy of its moods, and tones, and colours, modern landscape
art is realising for us pictorially what was realised in such plastic
perfection by the Greeks.  Music, in which all subject is absorbed in
expression and cannot be separated from it, is a complex example, and a
flower or a child a simple example, of what I mean; but sorrow is the
ultimate type both in life and art.

Behind joy and laughter there may be a temperament, coarse, hard and
callous.  But behind sorrow there is always sorrow.  Pain, unlike
pleasure, wears no mask.  Truth in art is not any correspondence between
the essential idea and the accidental existence; it is not the
resemblance of shape to shadow, or of the form mirrored in the crystal to
the form itself; it is no echo coming from a hollow hill, any more than
it is a silver well of water in the valley that shows the moon to the
moon and Narcissus to Narcissus.  Truth in art is the unity of a thing
with itself: the outward rendered expressive of the inward: the soul made
incarnate: the body instinct with spirit.  For this reason there is no
truth comparable to sorrow.  There are times when sorrow seems to me to
be the only truth.  Other things may be illusions of the eye or the
appetite, made to blind the one and cloy the other, but out of sorrow
have the worlds been built, and at the birth of a child or a star there
is pain.

More than this, there is about sorrow an intense, an extraordinary
reality.  I have said of myself that I was one who stood in symbolic
relations to the art and culture of my age.  There is not a single
wretched man in this wretched place along with me who does not stand in
symbolic relation to the very secret of life.  For the secret of life is
suffering.  It is what is hidden behind everything.  When we begin to
live, what is sweet is so sweet to us, and what is bitter so bitter, that
we inevitably direct all our desires towards pleasures, and seek not
merely for a 'month or twain to feed on honeycomb,' but for all our years
to taste no other food, ignorant all the while that we may really be
starving the soul.--_De Profundis_.




VITA NUOVA


Far off, like a perfect pearl, one can see the city of God.  It is so
wonderful that it seems as if a child could reach it in a summer's day.
And so a child could.  But with me and such as me it is different.  One
can realise a thing in a single moment, but one loses it in the long
hours that follow with leaden feet.  It is so difficult to keep 'heights
that the soul is competent to gain.'  We think in eternity, but we move
slowly through time; and how slowly time goes with us who lie in prison I
need not tell again, nor of the weariness and despair that creep back
into one's cell, and into the cell of one's heart, with such strange
insistence that one has, as it were, to garnish and sweep one's house for
their coming, as for an unwelcome guest, or a bitter master, or a slave
whose slave it is one's chance or choice to be.

And, though at present my friends may find it a hard thing to believe, it
is true none the less, that for them living in freedom and idleness and
comfort it is more easy to learn the lessons of humility than it is for
me, who begin the day by going down on my knees and washing the floor of
my cell.  For prison life with its endless privations and restrictions
makes one rebellious.  The most terrible thing about it is not that it
breaks one's heart--hearts are made to be broken--but that it turns one's
heart to stone.  One sometimes feels that it is only with a front of
brass and a lip of scorn that one can get through the day at all.  And he
who is in a state of rebellion cannot receive grace, to use the phrase of
which the Church is so fond--so rightly fond, I dare say--for in life as
in art the mood of rebellion closes up the channels of the soul, and
shuts out the airs of heaven.  Yet I must learn these lessons here, if I
am to learn them anywhere, and must be filled with joy if my feet are on
the right road and my face set towards 'the gate which is called
beautiful,' though I may fall many times in the mire and often in the
mist go astray.

This New Life, as through my love of Dante I like sometimes to call it,
is of course no new life at all, but simply the continuance, by means of
development, and evolution, of my former life.  I remember when I was at
Oxford saying to one of my friends as we were strolling round Magdalen's
narrow bird-haunted walks one morning in the year before I took my
degree, that I wanted to eat of the fruit of all the trees in the garden
of the world, and that I was going out into the world with that passion
in my soul.  And so, indeed, I went out, and so I lived.  My only mistake
was that I confined myself so exclusively to the trees of what seemed to
me the sun-lit side of the garden, and shunned the other side for its
shadow and its gloom.  Failure, disgrace, poverty, sorrow, despair,
suffering, tears even, the broken words that come from lips in pain,
remorse that makes one walk on thorns, conscience that condemns, self-
abasement that punishes, the misery that puts ashes on its head, the
anguish that chooses sack-cloth for its raiment and into its own drink
puts gall:--all these were things of which I was afraid.  And as I had
determined to know nothing of them, I was forced to taste each of them in
turn, to feed on them, to have for a season, indeed, no other food at
all.

I don't regret for a single moment having lived for pleasure.  I did it
to the full, as one should do everything that one does.  There was no
pleasure I did not experience.  I threw the pearl of my soul into a cup
of wine.  I went down the primrose path to the sound of flutes.  I lived
on honeycomb.  But to have continued the same life would have been wrong
because it would have been limiting.  I had to pass on.  The other half
of the garden had its secrets for me also.--_De Profundis_.




THE GRAND ROMANTIC


It is when he deals with a sinner that Christ is most romantic, in the
sense of most real.  The world had always loved the saint as being the
nearest possible approach to the perfection of God.  Christ, through some
divine instinct in him, seems to have always loved the sinner as being
the nearest possible approach to the perfection of man.  His primary
desire was not to reform people, any more than his primary desire was to
a relieve suffering.  To turn an interesting thief into a tedious honest
man was not his aim.  He would have thought little of the Prisoners' Aid
Society and other modern movements of the kind.  The conversion of a
publican into a Pharisee would not have seemed to him a great
achievement.  But in a manner not yet understood of the world he regarded
sin and suffering as being in themselves beautiful holy things and modes
of perfection.

It seems a very dangerous idea.  It is--all great ideas are dangerous.
That it was Christ's creed admits of no doubt.  That it is the true creed
I don't doubt myself.

Of course the sinner must repent.  But why?  Simply because otherwise he
would be unable to realise what he had done.  The moment of repentance is
the moment of initiation.  More than that: it is the means by which one
alters one's past.  The Greeks thought that impossible.  They often say
in their Gnomic aphorisms, 'Even the Gods cannot alter the past.'  Christ
showed that the commonest sinner could do it, that it was the one thing
he could do.  Christ, had he been asked, would have said--I feel quite
certain about it--that the moment the prodigal son fell on his knees and
wept, he made his having wasted his substance with harlots, his swine-
herding and hungering for the husks they ate, beautiful and holy moments
in his life.  It is difficult for most people to grasp the idea.  I dare
say one has to go to prison to understand it.  If so, it may be worth
while going to prison.

There is something so unique about Christ.  Of course just as there are
false dawns before the dawn itself, and winter days so full of sudden
sunlight that they will cheat the wise crocus into squandering its gold
before its time, and make some foolish bird call to its mate to build on
barren boughs, so there were Christians before Christ.  For that we
should be grateful.  The unfortunate thing is that there have been none
since.  I make one exception, St. Francis of Assisi.  But then God had
given him at his birth the soul of a poet, as he himself when quite young
had in mystical marriage taken poverty as his bride: and with the soul of
a poet and the body of a beggar he found the way to perfection not
difficult.  He understood Christ, and so he became like him.  We do not
require the Liber Conformitatum to teach us that the life of St. Francis
was the true _Imitatio Christi_, a poem compared to which the book of
that name is merely prose.

Indeed, that is the charm about Christ, when all is said: he is just like
a work of art.  He does not really teach one anything, but by being
brought into his presence one becomes something.  And everybody is
predestined to his presence.  Once at least in his life each man walks
with Christ to Emmaus.--_De Profundis_.




CLAPHAM JUNCTION


My lot has been one of public infamy, of long imprisonment, of misery, of
ruin, of disgrace, but I am not worthy of it--not yet, at any rate.  I
remember that I used to say that I thought I could bear a real tragedy if
it came to me with purple pall and a mask of noble sorrow, but that the
dreadful thing about modernity was that it put tragedy into the raiment
of comedy, so that the great realities seemed commonplace or grotesque or
lacking in style.  It is quite true about modernity.  It has probably
always been true about actual life.  It is said that all martyrdoms
seemed mean to the looker on.  The nineteenth century is no exception to
the rule.

Everything about my tragedy has been hideous, mean, repellent, lacking in
style; our very dress makes us grotesque.  We are the zanies of sorrow.
We are clowns whose hearts are broken.  We are specially designed to
appeal to the sense of humour.  On November 13th, 1895, I was brought
down here from London.  From two o'clock till half-past two on that day I
had to stand on the centre platform of Clapham Junction in convict dress,
and handcuffed, for the world to look at.  I had been taken out of the
hospital ward without a moment's notice being given to me.  Of all
possible objects I was the most grotesque.  When people saw me they
laughed.  Each train as it came up swelled the audience.  Nothing could
exceed their amusement.  That was, of course, before they knew who I was.
As soon as they had been informed they laughed still more.  For half an
hour I stood there in the grey November rain surrounded by a jeering
mob.--_De Profundis_.




THE BROKEN RESOLUTION


We call ours a utilitarian age, and we do not know the uses of any single
thing.  We have forgotten that water can cleanse, and fire purify, and
that the Earth is mother to us all.  As a consequence our art is of the
moon and plays with shadows, while Greek art is of the sun and deals
directly with things.  I feel sure that in elemental forces there is
purification, and I want to go back to them and live in their presence.

Of course to one so modern as I am, 'Enfant de mon siecle,' merely to
look at the world will be always lovely.  I tremble with pleasure when I
think that on the very day of my leaving prison both the laburnum and the
lilac will be blooming in the gardens, and that I shall see the wind stir
into restless beauty the swaying gold of the one, and make the other toss
the pale purple of its plumes, so that all the air shall be Arabia for
me.  Linnaeus fell on his knees and wept for joy when he saw for the
first time the long heath of some English upland made yellow with the
tawny aromatic brooms of the common furze; and I know that for me, to
whom flowers are part of desire, there are tears waiting in the petals of
some rose.  It has always been so with me from my boyhood.  There is not
a single colour hidden away in the chalice of a flower, or the curve of a
shell, to which, by some subtle sympathy with the very soul of things, my
nature does not answer.  Like Gautier, I have always been one of those
'pour qui le monde visible existe.'

Still, I am conscious now that behind all this beauty, satisfying though
it may be, there is some spirit hidden of which the painted forms and
shapes are but modes of manifestation, and it is with this spirit that I
desire to become in harmony.  I have grown tired of the articulate
utterances of men and things.  The Mystical in Art, the Mystical in Life,
the Mystical in Nature this is what I am looking for.  It is absolutely
necessary for me to find it somewhere.

All trials are trials for one's life, just as all sentences are sentences
of death; and three times have I been tried.  The first time I left the
box to be arrested, the second time to be led back to the house of
detention, the third time to pass into a prison for two years.  Society,
as we have constituted it, will have no place for me, has none to offer;
but Nature, whose sweet rains fall on unjust and just alike, will have
clefts in the rocks where I may hide, and secret valleys in whose silence
I may weep undisturbed.  She will hang the night with stars so that I may
walk abroad in the darkness without stumbling, and send the wind over my
footprints so that none may track me to my hurt: she will cleanse me in
great waters, and with bitter herbs make me whole.--_De Profundis_.




DOMESTICITY AT BERNEVAL


DIEPPE,

June 1st, 1897.

My Dear Robbie,--I propose to live at Berneval.  I will _not_ live in
Paris, nor in Algiers, nor in Southern Italy.  Surely a house for a year,
if I choose to continue there, at 32 pounds is absurdly cheap.  I could
not live cheaper at a hotel.  You are penny foolish, and pound foolish--a
dreadful state for my financier to be in.  I told M. Bonnet that my
bankers were MM. Ross et Cie, banquiers celebres de Londres--and now you
suddenly show me that you have no place among the great financial people,
and are afraid of any investment over 31 pounds, 10s.  It is merely the
extra ten shillings that baffles you.  As regards people living on me,
and the extra bedrooms: dear boy, there is no one who would stay with me
but you, and you will pay your own bill at the hotel for meals; and as
for your room, the charge will be nominally 2 francs 50 centimes a night,
but there will be lots of extras such as _bougie, bain_ and hot water,
and all cigarettes smoked in the bedrooms are charged extra.  And if any
one does not take the extras, of course he is charged more:--

   Bain, 25 C.

   Pas de bain, 50 C.

   Cigarette dans la chambre a coucher, 10 C. pour chaque cigarette.

   Pas de cigarette dans la chambre a coucher, 20 C. pour chaque
   cigarette.

This is the system at all good hotels.  If Reggie comes, of course he
will pay a little more: I cannot forget that he gave me a dressing-case.
Sphinxes pay a hundred per cent more than any one else--they always did
in Ancient Egypt.

But seriously, Robbie, if people stayed with me, of course they would pay
their _pension_ at the hotel.  They would have to: except architects.  A
modern architect, like modern architecture, doesn't pay.  But then I know
only one architect and you are hiding him somewhere from me.  I believe
that he is as extinct as the dado, of which now only fossil remains are
found, chiefly in the vicinity of Brompton, where they are sometimes
discovered by workmen excavating.  They are usually embedded in the old
Lincrusta Walton strata, and are rare consequently.

I visited M. le Cure {4} to-day.  He has a charming house and a _jardin
potager_.  He showed me over the church.  To-morrow I sit in the choir by
his special invitation.  He showed me all his vestments.  To-morrow he
really will be charming in red.  He knows I am a heretic, and believes
Pusey is still alive.  He says that God will convert England on account
of England's kindness to _les pretres exiles_ at the time of the
Revolution.  It is to be the reward of that sea-lashed island.

Stained glass windows are wanted in the church; he has only six; fourteen
more are needed.  He gets them at 300 francs--12 pounds--a window in
Paris.  I was nearly offering half a dozen, but remembered you, and so
only gave him something _pour les pauvres_.  You had a narrow escape,
Robbie.  You should be thankful.

I hope the 40 pounds is on its way, and that the 60 pounds will follow.  I
am going to hire a boat.  It will save walking and so be an economy in
the end.  Dear Robbie, I must start well.  If the life of St. Francis of
Assissi awaits me I shall not be angry.  Worse things might happen.

Yours,

OSCAR.

--_Letter to Robert Ross_.




A VISIT TO THE POPE


c/o COOK & SON, PIAZZA DI SPAGNA, ROME,

April 16th, 1900.

My dear Robbie,--I simply cannot write.  It is too horrid, not of me, but
to me.  It is a mode of paralysis--a _cacoethes tacendi_--the one form
that malady takes in me.

Well, all passed over very successfully.  Palermo, where we stayed eight
days, was lovely.  The most beautifully situated town in the world--it
dreams away its life in the _concha d'oro_, the exquisite valley that
lies between two seas.  The lemon groves and the orange gardens were so
entirely perfect that I became quite a Pre-Raphaelite, and loathed the
ordinary impressionists whose muddly souls and blurred intelligences
would have rendered, but by mud and blur, those "golden lamps hung in a
green night" that filled me with such joy.  The elaborate and exquisite
detail of the true Pre-Raphaelite is the compensation they offer us for
the absence of motion; literature and motion being the only arts that are
not immobile.

Then nowhere, not even at Ravenna, have I seen such mosaics as in the
Capella Palatine, which from pavement to domed ceiling is all gold: one
really feels as if one was sitting in the heart of a great honey-comb
looking at angels singing: and _looking_ at angels, or indeed at people,
singing, is much nicer than listening to them, for this reason: the great
artists always give to their angels lutes without strings, pipes without
vent-holes, and reeds through which no wind can wander or make
whistlings.

Monreale you have heard of--with its cloisters and cathedral: we often
drove there.

I also made great friends with a young seminarist, who lived in the
cathedral of Palermo--he and eleven others, in little rooms beneath the
roof, like birds.

Every day he showed me all over the cathedral, I knelt before the huge
porphyry sarcophagus in which Frederick the Second lies: it is a sublime
bare monstrous thing--blood-coloured, and held up by lions who have
caught some of the rage of the great Emperor's restless soul.  At first
my young friend, Giuseppe Loverdi, gave me information; but on the third
day I gave information to him, and re-wrote history as usual, and told
him all about the supreme King and his Court of Poets, and the terrible
book that he never wrote.  His reason for entering the church was
singularly mediaeval.  I asked him why he thought of becoming a
_clerico_, and how.  He answered: "My father is a cook and most poor; and
we are many at home, so it seemed to me a good thing that there should be
in so small a house as ours, one mouth less to feed; for though I am
slim, I eat much, too much, alas! I fear."

I told him to be comforted, because God used poverty often as a means of
bringing people to Him, and used riches never, or rarely; so Giuseppe was
comforted, and I gave him a little book of devotion, very pretty, and
with far more pictures than prayers in it--so of great service to
Giuseppe whose eyes are beautiful.  I also gave him many _lire_, and
prophesied for him a Cardinal's hat, if he remained very good and never
forgot me.

At Naples we stopped three days: most of my friends are, as you know, in
prison, but I met some of nice memory.

We came to Rome on Holy Thursday.  H--- left on Saturday for Gland--and
yesterday, to the terror of Grissell {5} and all the Papal Court, I
appeared in the front rank of the pilgrims in the Vatican, and got the
blessing of the Holy Father--a blessing they would have denied me.

He was wonderful as he was carried past me on his throne--not of flesh
and blood, but a white soul robed in white and an artist as well as a
saint--the only instance in history, if the newspapers are to be
believed.  I have seen nothing like the extraordinary grace of his
gestures as he rose, from moment to moment, to bless--possibly the
pilgrims, but certainly me.

Tree should see him.  It is his only chance.

I was deeply impressed, and my walking-stick showed signs of budding,
would have budded, indeed, only at the door of the Chapel it was taken
from me by the Knave of Spades.  This strange prohibition is, of course,
in honour of Tannhauser.

How did I get the ticket?  By a miracle, of course.  I thought it was
hopeless and made no effort of any kind.  On Saturday afternoon at five
o'clock H--- and I went to have tea at the Hotel de l'Europe.  Suddenly,
as I was eating buttered toast, a man--or what seemed to be one--dressed
like a hotel porter entered and asked me would I like to see the Pope on
Easter Day.  I bowed my head humbly and said "Non sum dignus," or words
to that effect.  He at once produced a ticket!

When I tell you that his countenance was of supernatural ugliness, and
that the price of the ticket was thirty pieces of silver, I need say no
more.

An equally curious thing is that whenever I pass the hotel, which I do
constantly, I see the same man.  Scientists call that phenomenon an
obsession of the visual nerve.  You and I know better.

On the afternoon of Easter Day I heard Vespers at the Lateran: music
quite lovely.  At the close, a Bishop in red, and with red gloves--such
as Pater talks of in _Gaston de Latour_--came out on the balcony and
showed us the Relics.  He was swarthy, and wore a yellow mitre.  A
sinister mediaeval man, but superbly Gothic, just like the bishops carved
on stalls or on portals: and when one thinks that once people mocked at
stained-glass attitudes! they are the only attitudes for the clothes.  The
sight of the Bishop, whom I watched with fascination, filled me with the
great sense of the realism of Gothic art.  Neither in Greek art nor in
Gothic art is there any pose.  Posing was invented by bad
portrait-painters; and the first person who posed was a stock-broker, and
he has gone on posing ever since.

I send you a photograph I took on Palm Sunday at Palermo.  Do send me
some of yours, and love me always, and try to read this letter.

Kindest regards to your dear mother.

Always,

OSCAR.

--_Letter to Robert Ross_.




FOOTNOTES


{1}  "The Influence of Pater and Matthew Arnold in the Prose-Writings of
Oscar Wilde," by Ernst Bendz.  London: H. Grevel & Co., 1914.

{2}  "The Eighteen Nineties: A Review of Art and Idea at the Close of the
Nineteenth Century," by Holbrook Jackson.  London: Grant Richards Ltd.,
1913.

{3} Mortimer Menpes.

{4}  M. Constant Trop-Hardy, died at Berneval, March 2, 1898.

{5}  Hartwell de la Garde Grissell, a Papal Chamberlain.



***END OF THE PROJECT GUTENBERG EBOOK SELECTED PROSE OF OSCAR WILDE***


******* This file should be named 1338.txt or 1338.zip *******


This and all associated files of various formats will be found in:
http://www.gutenberg.org/dirs/1/3/3/1338



Updated editions will replace the previous one--the old editions
will be renamed.

Creating the works from public domain print editions means that no
one owns a United States copyright in these works, so the Foundation
(and you!) can copy and distribute it in the United States without
permission and without paying copyright royalties.  Special rules,
set forth in the General Terms of Use part of this license, apply to
copying and distributing Project Gutenberg-tm electronic works to
protect the PROJECT GUTENBERG-tm concept and trademark.  Project
Gutenberg is a registered trademark, and may not be used if you
charge for the eBooks, unless you receive specific permission.  If you
do not charge anything for copies of this eBook, complying with the
rules is very easy.  You may use this eBook for nearly any purpose
such as creation of derivative works, reports, performances and
research.  They may be modified and printed and given away--you may do
practically ANYTHING with public domain eBooks.  Redistribution is
subject to the trademark license, especially commercial
redistribution.



*** START: FULL LICENSE ***

THE FULL PROJECT GUTENBERG LICENSE
PLEASE READ THIS BEFORE YOU DISTRIBUTE OR USE THIS WORK

To protect the Project Gutenberg-tm mission of promoting the free
distribution of electronic works, by using or distributing this work
(or any other work associated in any way with the phrase "Project
Gutenberg"), you agree to comply with all the terms of the Full Project
Gutenberg-tm License (available with this file or online at
http://gutenberg.net/license).


Section 1.  General Terms of Use and Redistributing Project Gutenberg-tm
electronic works

1.A.  By reading or using any part of this Project Gutenberg-tm
electronic work, you indicate that you have read, understand, agree to
and accept all the terms of this license and intellectual property
(trademark/copyright) agreement.  If you do not agree to abide by all
the terms of this agreement, you must cease using and return or destroy
all copies of Project Gutenberg-tm electronic works in your possession.
If you paid a fee for obtaining a copy of or access to a Project
Gutenberg-tm electronic work and you do not agree to be bound by the
terms of this agreement, you may obtain a refund from the person or
entity to whom you paid the fee as set forth in paragraph 1.E.8.

1.B.  "Project Gutenberg" is a registered trademark.  It may only be
used on or associated in any way with an electronic work by people who
agree to be bound by the terms of this agreement.  There are a few
things that you can do with most Project Gutenberg-tm electronic works
even without complying with the full terms of this agreement.  See
paragraph 1.C below.  There are a lot of things you can do with Project
Gutenberg-tm electronic works if you follow the terms of this agreement
and help preserve free future access to Project Gutenberg-tm electronic
works.  See paragraph 1.E below.

1.C.  The Project Gutenberg Literary Archive Foundation ("the Foundation"
or PGLAF), owns a compilation copyright in the collection of Project
Gutenberg-tm electronic works.  Nearly all the individual works in the
collection are in the public domain in the United States.  If an
individual work is in the public domain in the United States and you are
located in the United States, we do not claim a right to prevent you from
copying, distributing, performing, displaying or creating derivative
works based on the work as long as all references to Project Gutenberg
are removed.  Of course, we hope that you will support the Project
Gutenberg-tm mission of promoting free access to electronic works by
freely sharing Project Gutenberg-tm works in compliance with the terms of
this agreement for keeping the Project Gutenberg-tm name associated with
the work.  You can easily comply with the terms of this agreement by
keeping this work in the same format with its attached full Project
Gutenberg-tm License when you share it without charge with others.

1.D.  The copyright laws of the place where you are located also govern
what you can do with this work.  Copyright laws in most countries are in
a constant state of change.  If you are outside the United States, check
the laws of your country in addition to the terms of this agreement
before downloading, copying, displaying, performing, distributing or
creating derivative works based on this work or any other Project
Gutenberg-tm work.  The Foundation makes no representations concerning
the copyright status of any work in any country outside the United
States.

1.E.  Unless you have removed all references to Project Gutenberg:

1.E.1.  The following sentence, with active links to, or other immediate
access to, the full Project Gutenberg-tm License must appear prominently
whenever any copy of a Project Gutenberg-tm work (any work on which the
phrase "Project Gutenberg" appears, or with which the phrase "Project
Gutenberg" is associated) is accessed, displayed, performed, viewed,
copied or distributed:

This eBook is for the use of anyone anywhere at no cost and with
almost no restrictions whatsoever.  You may copy it, give it away or
re-use it under the terms of the Project Gutenberg License included
with this eBook or online at www.gutenberg.net

1.E.2.  If an individual Project Gutenberg-tm electronic work is derived
from the public domain (does not contain a notice indicating that it is
posted with permission of the copyright holder), the work can be copied
and distributed to anyone in the United States without paying any fees
or charges.  If you are redistributing or providing access to a work
with the phrase "Project Gutenberg" associated with or appearing on the
work, you must comply either with the requirements of paragraphs 1.E.1
through 1.E.7 or obtain permission for the use of the work and the
Project Gutenberg-tm trademark as set forth in paragraphs 1.E.8 or
1.E.9.

1.E.3.  If an individual Project Gutenberg-tm electronic work is posted
with the permission of the copyright holder, your use and distribution
must comply with both paragraphs 1.E.1 through 1.E.7 and any additional
terms imposed by the copyright holder.  Additional terms will be linked
to the Project Gutenberg-tm License for all works posted with the
permission of the copyright holder found at the beginning of this work.

1.E.4.  Do not unlink or detach or remove the full Project Gutenberg-tm
License terms from this work, or any files containing a part of this
work or any other work associated with Project Gutenberg-tm.

1.E.5.  Do not copy, display, perform, distribute or redistribute this
electronic work, or any part of this electronic work, without
prominently displaying the sentence set forth in paragraph 1.E.1 with
active links or immediate access to the full terms of the Project
Gutenberg-tm License.

1.E.6.  You may convert to and distribute this work in any binary,
compressed, marked up, nonproprietary or proprietary form, including any
word processing or hypertext form.  However, if you provide access to or
distribute copies of a Project Gutenberg-tm work in a format other than
"Plain Vanilla ASCII" or other format used in the official version
posted on the official Project Gutenberg-tm web site (www.gutenberg.net),
you must, at no additional cost, fee or expense to the user, provide a
copy, a means of exporting a copy, or a means of obtaining a copy upon
request, of the work in its original "Plain Vanilla ASCII" or other
form.  Any alternate format must include the full Project Gutenberg-tm
License as specified in paragraph 1.E.1.

1.E.7.  Do not charge a fee for access to, viewing, displaying,
performing, copying or distributing any Project Gutenberg-tm works
unless you comply with paragraph 1.E.8 or 1.E.9.

1.E.8.  You may charge a reasonable fee for copies of or providing
access to or distributing Project Gutenberg-tm electronic works provided
that

- You pay a royalty fee of 20% of the gross profits you derive from
     the use of Project Gutenberg-tm works calculated using the method
     you already use to calculate your applicable taxes.  The fee is
     owed to the owner of the Project Gutenberg-tm trademark, but he
     has agreed to donate royalties under this paragraph to the
     Project Gutenberg Literary Archive Foundation.  Royalty payments
     must be paid within 60 days following each date on which you
     prepare (or are legally required to prepare) your periodic tax
     returns.  Royalty payments should be clearly marked as such and
     sent to the Project Gutenberg Literary Archive Foundation at the
     address specified in Section 4, "Information about donations to
     the Project Gutenberg Literary Archive Foundation."

- You provide a full refund of any money paid by a user who notifies
     you in writing (or by e-mail) within 30 days of receipt that s/he
     does not agree to the terms of the full Project Gutenberg-tm
     License.  You must require such a user to return or
     destroy all copies of the works possessed in a physical medium
     and discontinue all use of and all access to other copies of
     Project Gutenberg-tm works.

- You provide, in accordance with paragraph 1.F.3, a full refund of any
     money paid for a work or a replacement copy, if a defect in the
     electronic work is discovered and reported to you within 90 days
     of receipt of the work.

- You comply with all other terms of this agreement for free
     distribution of Project Gutenberg-tm works.

1.E.9.  If you wish to charge a fee or distribute a Project Gutenberg-tm
electronic work or group of works on different terms than are set
forth in this agreement, you must obtain permission in writing from
both the Project Gutenberg Literary Archive Foundation and Michael
Hart, the owner of the Project Gutenberg-tm trademark.  Contact the
Foundation as set forth in Section 3 below.

1.F.

1.F.1.  Project Gutenberg volunteers and employees expend considerable
effort to identify, do copyright research on, transcribe and proofread
public domain works in creating the Project Gutenberg-tm
collection.  Despite these efforts, Project Gutenberg-tm electronic
works, and the medium on which they may be stored, may contain
"Defects," such as, but not limited to, incomplete, inaccurate or
corrupt data, transcription errors, a copyright or other intellectual
property infringement, a defective or damaged disk or other medium, a
computer virus, or computer codes that damage or cannot be read by
your equipment.

1.F.2.  LIMITED WARRANTY, DISCLAIMER OF DAMAGES - Except for the "Right
of Replacement or Refund" described in paragraph 1.F.3, the Project
Gutenberg Literary Archive Foundation, the owner of the Project
Gutenberg-tm trademark, and any other party distributing a Project
Gutenberg-tm electronic work under this agreement, disclaim all
liability to you for damages, costs and expenses, including legal
fees.  YOU AGREE THAT YOU HAVE NO REMEDIES FOR NEGLIGENCE, STRICT
LIABILITY, BREACH OF WARRANTY OR BREACH OF CONTRACT EXCEPT THOSE
PROVIDED IN PARAGRAPH F3.  YOU AGREE THAT THE FOUNDATION, THE
TRADEMARK OWNER, AND ANY DISTRIBUTOR UNDER THIS AGREEMENT WILL NOT BE
LIABLE TO YOU FOR ACTUAL, DIRECT, INDIRECT, CONSEQUENTIAL, PUNITIVE OR
INCIDENTAL DAMAGES EVEN IF YOU GIVE NOTICE OF THE POSSIBILITY OF SUCH
DAMAGE.

1.F.3.  LIMITED RIGHT OF REPLACEMENT OR REFUND - If you discover a
defect in this electronic work within 90 days of receiving it, you can
receive a refund of the money (if any) you paid for it by sending a
written explanation to the person you received the work from.  If you
received the work on a physical medium, you must return the medium with
your written explanation.  The person or entity that provided you with
the defective work may elect to provide a replacement copy in lieu of a
refund.  If you received the work electronically, the person or entity
providing it to you may choose to give you a second opportunity to
receive the work electronically in lieu of a refund.  If the second copy
is also defective, you may demand a refund in writing without further
opportunities to fix the problem.

1.F.4.  Except for the limited right of replacement or refund set forth
in paragraph 1.F.3, this work is provided to you 'AS-IS', WITH NO OTHER
WARRANTIES OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO
WARRANTIES OF MERCHANTIBILITY OR FITNESS FOR ANY PURPOSE.

1.F.5.  Some states do not allow disclaimers of certain implied
warranties or the exclusion or limitation of certain types of damages.
If any disclaimer or limitation set forth in this agreement violates the
law of the state applicable to this agreement, the agreement shall be
interpreted to make the maximum disclaimer or limitation permitted by
the applicable state law.  The invalidity or unenforceability of any
provision of this agreement shall not void the remaining provisions.

1.F.6.  INDEMNITY - You agree to indemnify and hold the Foundation, the
trademark owner, any agent or employee of the Foundation, anyone
providing copies of Project Gutenberg-tm electronic works in accordance
with this agreement, and any volunteers associated with the production,
promotion and distribution of Project Gutenberg-tm electronic works,
harmless from all liability, costs and expenses, including legal fees,
that arise directly or indirectly from any of the following which you do
or cause to occur: (a) distribution of this or any Project Gutenberg-tm
work, (b) alteration, modification, or additions or deletions to any
Project Gutenberg-tm work, and (c) any Defect you cause.


Section  2.  Information about the Mission of Project Gutenberg-tm

Project Gutenberg-tm is synonymous with the free distribution of
electronic works in formats readable by the widest variety of computers
including obsolete, old, middle-aged and new computers.  It exists
because of the efforts of hundreds of volunteers and donations from
people in all walks of life.

Volunteers and financial support to provide volunteers with the
assistance they need, is critical to reaching Project Gutenberg-tm's
goals and ensuring that the Project Gutenberg-tm collection will
remain freely available for generations to come.  In 2001, the Project
Gutenberg Literary Archive Foundation was created to provide a secure
and permanent future for Project Gutenberg-tm and future generations.
To learn more about the Project Gutenberg Literary Archive Foundation
and how your efforts and donations can help, see Sections 3 and 4
and the Foundation web page at http://www.gutenberg.net/fundraising/pglaf.


Section 3.  Information about the Project Gutenberg Literary Archive
Foundation

The Project Gutenberg Literary Archive Foundation is a non profit
501(c)(3) educational corporation organized under the laws of the
state of Mississippi and granted tax exempt status by the Internal
Revenue Service.  The Foundation's EIN or federal tax identification
number is 64-6221541.  Contributions to the Project Gutenberg
Literary Archive Foundation are tax deductible to the full extent
permitted by U.S. federal laws and your state's laws.

The Foundation's principal office is located at 4557 Melan Dr. S.
Fairbanks, AK, 99712., but its volunteers and employees are scattered
throughout numerous locations.  Its business office is located at
809 North 1500 West, Salt Lake City, UT 84116, (801) 596-1887, email
business@pglaf.org.  Email contact links and up to date contact
information can be found at the Foundation's web site and official
page at http://www.gutenberg.net/about/contact

For additional contact information:
     Dr. Gregory B. Newby
     Chief Executive and Director
     gbnewby@pglaf.org

Section 4.  Information about Donations to the Project Gutenberg
Literary Archive Foundation

Project Gutenberg-tm depends upon and cannot survive without wide
spread public support and donations to carry out its mission of
increasing the number of public domain and licensed works that can be
freely distributed in machine readable form accessible by the widest
array of equipment including outdated equipment.  Many small donations
($1 to $5,000) are particularly important to maintaining tax exempt
status with the IRS.

The Foundation is committed to complying with the laws regulating
charities and charitable donations in all 50 states of the United
States.  Compliance requirements are not uniform and it takes a
considerable effort, much paperwork and many fees to meet and keep up
with these requirements.  We do not solicit donations in locations
where we have not received written confirmation of compliance.  To
SEND DONATIONS or determine the status of compliance for any
particular state visit http://www.gutenberg.net/fundraising/donate

While we cannot and do not solicit contributions from states where we
have not met the solicitation requirements, we know of no prohibition
against accepting unsolicited donations from donors in such states who
approach us with offers to donate.

International donations are gratefully accepted, but we cannot make
any statements concerning tax treatment of donations received from
outside the United States.  U.S. laws alone swamp our small staff.

Please check the Project Gutenberg Web pages for current donation
methods and addresses.  Donations are accepted in a number of other
ways including including checks, online payments and credit card
donations.  To donate, please visit:
http://www.gutenberg.net/fundraising/donate


Section 5.  General Information About Project Gutenberg-tm electronic
works.

Professor Michael S. Hart is the originator of the Project Gutenberg-tm
concept of a library of electronic works that could be freely shared
with anyone.  For thirty years, he produced and distributed Project
Gutenberg-tm eBooks with only a loose network of volunteer support.

Project Gutenberg-tm eBooks are often created from several printed
editions, all of which are confirmed as Public Domain in the U.S.
unless a copyright notice is included.  Thus, we do not necessarily
keep eBooks in compliance with any particular paper edition.

Most people start at our Web site which has the main PG search facility:

     http://www.gutenberg.net

This Web site includes information about Project Gutenberg-tm,
including how to make donations to the Project Gutenberg Literary
Archive Foundation, how to help produce our new eBooks, and how to
subscribe to our email newsletter to hear about new eBooks.'''
#
#
#
#  punc_list = [".",";",":","!","?","/","\\",",","#","@","$","&",")","(","'","\""]
#  no_punc = ''
#  for i in punc_list:
#      if i not in punc_list:
#          no_punc += i
#      else:
#          no_punc += ' '

# return no_punc.lower()
#
#
#
#
#
# WORKS
# Text = Text.lower()
# Text = Text.split()
# print(Text)
#


#
#
# Counter(text).most_common()
# Text = list(word_dict.items())  # .items() returns a list of tuples
# text.sort(key=lambda tup: tup[1], reverse=True)  # sort largest to smallest, based on count


