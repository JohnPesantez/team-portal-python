def test_get_news(client):
    response = client.get("/news")

    assert response.status_code == 200

def test_get_single_news(client, create_news):
   
   
    response = client.get(f"/news/{create_news}")

    assert response.status_code == 200

def test_create_news(client):
    post_data = {
        "title" : "This news is a test",
        "description" : "a pay rise will happen on June 2027 to all employees",
        "is_announcement" : True
    }

    response = client.post("/news", json = post_data)

    assert response.status_code == 200

def test_update_news(client, create_news):
    post_data = {
        "title" : "This news is a test",
        "description" : "a pay rise will happen on June 2027 to all employees",
        "is_announcement" : False
    }

    response = client.put(f"/news/{create_news}",json = post_data)

    assert response.status_code == 200

def test_patch_news(client, create_news):
    post_data = {
        "title" : "Pay rise alert",
   }

    response = client.patch(f"/news/{create_news}", json = post_data)

    assert response.status_code == 200

def test_delete_news(client, create_news):
    response = client.delete(f"/news/{create_news}")

    assert response.status_code == 200