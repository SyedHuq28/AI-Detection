from binoculars import Binoculars

bino = Binoculars()

# ChatGPT (GPT-4) output when prompted with “Can you write a few sentences about a capybara that is an astrophysicist?"
sample_string = '''Dr. Capy Cosmos, a capybara unlike any other, astounded the scientific'''

#print(bino.compute_score(sample_string))  # 0.75661373
#print(bino.predict(sample_string))  # 'Most likely AI-Generated'

def sliding_window(text):
    words = text.split()
    for i in range(3, len(words) + 1):
        yield ' '.join(words[:i])

sample_string = '''Dr. Capy Cosmos, a capybara unlike any other, astounded the scientific'''
sliding_texts = list(sliding_window(sample_string))

for text in sliding_texts:
    print(text.strip(), "-", bino.compute_score(text))