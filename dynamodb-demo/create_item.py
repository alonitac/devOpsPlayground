import boto3

# IMPORTANT change to your region
region = 'us-east-1'


def put_movie(title, year, plot, rating):
    dynamodb = boto3.resource('dynamodb', region_name=region)
    table = dynamodb.Table('Movies')
    response = table.put_item(
        Item={
            'year': year,
            'title': title,
            'info': {
                'plot': plot,
                'rating': rating
            }
        }
    )
    return response


if __name__ == '__main__':
    movie_resp = put_movie("The Big New Movie", '2015', "Nothing happens at all.", '0')
    print("Put movie succeeded:")
