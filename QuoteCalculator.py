from config import *

def get_importance_score(sorted_topics):
    '''
    Get the dictionary of importance score of requested topics

    sorted_topics(dict): dictionary of top 3 requested topics

    return (dict): dictionary of top 3 requested topics with the importance values 
    '''
    topic_importance_keys = list(sorted_topics.keys())
    return dict(zip(topic_importance_keys, topic_importance_values))

class QuoteCalculator():
    '''
    Class to calculate final quotes from provider's available topics based on requested topics
    '''
    def __init__(self, data, provider_topics):
        '''
        data (dict): dictionary containing data of requested topics
        provider_topics (dict): dictionary containing data of provider's available topics
        '''
        self.sorted_topics = dict(sorted(data["topics"].items(), key=lambda item: item[1], reverse=True)[:3])
        self.provider_topics = provider_topics

    def get_final_quotes(self):
        '''
        Calculate final quotes from provider's available topics based on requested topics

        return (dict): dictionary containing the final quotes
        '''
        # Get the importance score
        topic_importance = get_importance_score(self.sorted_topics)

        final_quotes = {}

        # for each provider's offered topics
        for provider, topics_str in self.provider_topics.items():
            provider_topic_set = set(topics_str.split("+"))
            matched_topics = provider_topic_set.intersection(self.sorted_topics.keys())

            # if 2 topics are matched
            if len(matched_topics) == 2:
                topics_content = sum(self.sorted_topics[topic] for topic in matched_topics)
                quote = 0.1 * topics_content
                final_quotes[provider] = round(quote, 2)

            # if 1 topic is matched
            elif len(matched_topics) == 1:
                topic = matched_topics.pop()
                # based on the importance score
                quote = topic_importance[topic] * self.sorted_topics[topic]
                final_quotes[provider] = round(quote, 2)

        return final_quotes