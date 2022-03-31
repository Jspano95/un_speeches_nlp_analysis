def display_topics(model, features, top_words=5):
    for topic, word_vector in enumerate(model.components_):

        #calculate the sum of the vector so we can later get the % contribution of individual words 
        total = word_vector.sum()

        # invert sort order (put index of largest value first)
        largest = word_vector.argsort()[::-1] 

        # print header 
        print("\nTopic %02d" % topic)

        # loop through top words (# specified number of {})
        for i in range(0, top_words):
            print("  %s (%2.2f)" % (features[largest[i]],
                  word_vector[largest[i]]*100.0/total)) # print contribution/total as %