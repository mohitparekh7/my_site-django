from django.shortcuts import render
from datetime import date, time

all_posts = [
    {
        "slug" : "hike-in-the-mountains",
        "image": "mountains.jpg",
        "author": "Mohit",
        "date": date(2021, 8 , 17),
        "title": "Mountain Hiking",
        "excerpt":"There's nothing like the views you get when hiking in the mountains And I wasnt even prepared for what happened whilst i was enjoying the view!",
        "content" : """
                    Lorem ipsum dolor sit amet consectetur adipisicing elit. Deleniti voluptatem nihil 
            possimus maxime tempora reprehenderit veniam dolorum delectus architecto nesciunt 
            debitis modi cum ipsa saepe nostrum est, adipisci quisquam qui.

            Lorem ipsum dolor sit amet consectetur adipisicing elit. Deleniti voluptatem nihil 
            possimus maxime tempora reprehenderit veniam dolorum delectus architecto nesciunt 
            debitis modi cum ipsa saepe nostrum est, adipisci quisquam qui.

            Lorem ipsum dolor sit amet consectetur adipisicing elit. Deleniti voluptatem nihil 
            possimus maxime tempora reprehenderit veniam dolorum delectus architecto nesciunt 
            debitis modi cum ipsa saepe nostrum est, adipisci quisquam qui.
        """,
    },
    {
        "slug" : "programming-is-fun",
        "image": "coding.jpg",
        "author": "Mohit",
        "date": date(2021, 8 , 29),
        "title": "Programming is Great",
        "excerpt":"Did you ever spend hours searching that one error in your code ? Yes ",
        "content" : """
                    Lorem ipsum dolor sit amet consectetur adipisicing elit. Deleniti voluptatem nihil 
            possimus maxime tempora reprehenderit veniam dolorum delectus architecto nesciunt 
            debitis modi cum ipsa saepe nostrum est, adipisci quisquam qui.

            Lorem ipsum dolor sit amet consectetur adipisicing elit. Deleniti voluptatem nihil 
            possimus maxime tempora reprehenderit veniam dolorum delectus architecto nesciunt 
            debitis modi cum ipsa saepe nostrum est, adipisci quisquam qui.

            Lorem ipsum dolor sit amet consectetur adipisicing elit. Deleniti voluptatem nihil 
            possimus maxime tempora reprehenderit veniam dolorum delectus architecto nesciunt 
            debitis modi cum ipsa saepe nostrum est, adipisci quisquam qui.
        """,
    },
    {
        "slug" : "into-the-woods",
        "image": "woods.jpg",
        "author": "Mohit",
        "date": date(2020, 4 , 1),
        "title": "Nature At its Best",
        "excerpt":"Nature is Amazing! THe amount of inspiration i get when walking in the nature",
        "content" : """
                    Lorem ipsum dolor sit amet consectetur adipisicing elit. Deleniti voluptatem nihil 
            possimus maxime tempora reprehenderit veniam dolorum delectus architecto nesciunt 
            debitis modi cum ipsa saepe nostrum est, adipisci quisquam qui.

            Lorem ipsum dolor sit amet consectetur adipisicing elit. Deleniti voluptatem nihil 
            possimus maxime tempora reprehenderit veniam dolorum delectus architecto nesciunt 
            debitis modi cum ipsa saepe nostrum est, adipisci quisquam qui.

            Lorem ipsum dolor sit amet consectetur adipisicing elit. Deleniti voluptatem nihil 
            possimus maxime tempora reprehenderit veniam dolorum delectus architecto nesciunt 
            debitis modi cum ipsa saepe nostrum est, adipisci quisquam qui.
        """,
    },
]

def get_date(post):
    return post.get('date')

# Create your views here. 

def starting_page(request):
    sorted_posts = sorted(all_posts, key=get_date)
    latest_posts = sorted_posts[-3:]
    return render(request,"blog/index.html", {
        "posts": latest_posts
    })

def posts(request):
    return render(request, "blog/all-posts.html", {
        "all_posts": all_posts,
    })

def post_detail(request,  slug):
    identified_post = next(post for post in all_posts if post['slug'] == slug)
    return render(request, "blog/post-detail.html",{
        "post": identified_post,
    })