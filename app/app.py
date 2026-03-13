from fastapi import FastAPI, HTTPException

from app.schemas import PostCreate, PostResponse

app = FastAPI()

text_posts = {
    1: {"title": "Post 1", "content": "This is post 1"},
    2: {"title": "Post 2", "content": "This is post 2"}
}

@app.get("/posts")
def get_all_posts(limit: int = None):
    if limit:
        return list(text_posts.values())[:limit]
    return text_posts

@app.get("/posts/{id}")
def get_post(id: int) -> PostResponse:
    if id not in text_posts:
        raise HTTPException(status_code=404, detail="Post not found")
    
    return text_posts.get(id)

@app.post("/posts")
def create_post(post: PostCreate) -> PostResponse:
    new_post = {
        "title": post.title,
        "content": post.message
    }
    text_posts[max(text_posts.keys())+1] = new_post
    return new_post