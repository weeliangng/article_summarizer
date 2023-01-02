from transformers import pipeline

summarizer = pipeline("summarization", model="facebook/bart-large-cnn")

print(summarizer(
    """
    SINGAPORE: Trash or treasure? While many charities get a bump in donations around the end of the year, a good chunk of "donations" in-kind can be unusable.
Dirty and worn clothing, broken appliances or toys, and damaged household items or belongings that are inappropriate for the beneficiaries are some examples.
One charity, SiloamXperience Outreach, said that they have also received damaged bags, incomplete sets of puzzles and earrings. Of the items they get, about 30 per cent to 40 per cent cannot be reused.
The not-for-profit organisation (NPO) runs a thrift store under its Trash to Treasure (t2t) project, and tries as much as possible to recycle and refashion items donated to them.
The proceeds from the thrift store go towards supporting its causes, such as improving the living standards of underprivileged communities.
A spokesperson said that the team will think of how to "creatively upcycle and repurpose" items that are donated, even if they may seem unusable at first.
"Someone gave us 16 cartons of mouldy tee-shirts, we upcycled them to grocery carriers or fashion vests ...  We turned old bookshelves and donated SIA crew used sheets into changing rooms which saved us about S$400," said the spokesperson.
"We are committed to create less waste thus taking steps to turn trash to treasure."
But that does not mean that it's okay to send your trash to charities. Non-government organisation (NGO) It's Raining Raincoats (IRR) just gave out about 10,000 gifts to migrant workers from donors for its fifth annual Christmas drive.
The presents included thousands of brand-new backpacks, snacks, hundreds of toothbrushes and toothpaste, water bottles and some umbrellas.
There were also used appliances such as rice cookers, kettles, ovens and toasters.


While there have been thousands of good donations, IRR said that it has got some "surprises" since it opened the inspIRRe store, a free shop for migrant workers, in September.

"We have gotten a few ‘surprises’ such as sex toys, clothing smelling like vomit, men’s preloved underwear, women’s lingerie, dirty shoes with holes, missing insoles, worn out treads,  female and kids clothes (not appropriate for our male migrant worker beneficiaries), expired N95 masks," said a spokesperson.

It then take additional time and manpower to dispose of some items. "This taxes on our limited manpower as IRR is almost entirely run by volunteers."

They also do not encourage people to donate clothes as the workers do not have much space in their dormitories for clothes. 

"They only take what they need. This means they only really want clothes in pristine condition."

On a recent social media post, IRR said: "We ask that people don’t pass us anything they themselves would not like to receive were they in need of it. This is to respect the basic dignity of our migrant workers."

The spokesperson added: "One man’s trash is NOT another man’s treasure."
"""
))