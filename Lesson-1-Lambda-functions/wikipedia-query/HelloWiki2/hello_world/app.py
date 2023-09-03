import json
import wikipedia
import wikipediaapi

# prints when function loads
print('Loading function')


def lambda_handler(event, context):
    ''' Wikipedia page summarizer.
        :param event: a request with a wikipedia "entity" that has page information
        :return: a response that contains the first sentence of a wikipedia page,
            the response is JSON formatted.'''
    
    ## TO DO: Check that the request has some input body and save it

    if 'body' in event:
        event = json.loads(event["body"])
        
    statusCode = 200;
    
    ## TO DO: Get the wikipedia "entity" from the body of the request
    if event == None:
        return {
        "statusCode": 400, 
        "headers": { "Content-type": "application/json" },
        "body": json.dumps({"message": "Null body"})
        }
        
    entity = event["entity"]
    
    wiki_wiki = wikipediaapi.Wikipedia('HelloWiki2 (trantheduyk13@gmail.com)', 'vi')
    res = wiki_wiki.page(entity).summary

    # res = wikipedia.summary(entity, sentences=1) # first sentence, result

    # print statements
    print(f"context: {context}, event: {event}")
    print(f"Response from wikipedia API: {res}")
    
    ## TO DO: Format the response as JSON and return the result
    print(json.dumps({"message":"xin chào việt nam"}, ensure_ascii=False))
    print(json.dumps({"message": res}, ensure_ascii=False))
    response = {
        "statusCode": statusCode, 
        "headers": { "Content-type": "application/json; charset=utf-8" },
        "body": json.dumps({"message": res}, ensure_ascii=True).encode('utf-8')
    }
    
    return response