from mongoengine import *
class Face(Document):
    hairstyle = ListField()
import mlab
mlab.connect()
diamond_face   = Face(
    hairstyle = [
        {"name":"Clean shaven head",
        "image_url":"https://2x1dks3q6aoj44bz1r1tr92f-wpengine.netdna-ssl.com/wp-content/uploads/2017/07/What-Is-A-Mens-Shaved-Head-Style.png"
        },
        {
            "name":"Buzz cut hairstyle",
            "image_url":"https://2x1dks3q6aoj44bz1r1tr92f-wpengine.netdna-ssl.com/wp-content/uploads/2017/07/What-Is-A-Buzz-Cut-Hairstyle-Graphic.png"
        },
        {
            "name":"Comb over hair style",
            "image_url":"https://2x1dks3q6aoj44bz1r1tr92f-wpengine.netdna-ssl.com/wp-content/uploads/2017/07/What-Is-A-Comb-Over-Hairstyle-Graphic.png"
        },
        {
            "name":"Fringe hair style",
            "image_url":"https://2x1dks3q6aoj44bz1r1tr92f-wpengine.netdna-ssl.com/wp-content/uploads/2017/07/What-Is-A-Fringe-Hairstyle-Graphic.png"
        },
        {
            "name":"Man bun hairstyle",
            "image_urk":"https://2x1dks3q6aoj44bz1r1tr92f-wpengine.netdna-ssl.com/wp-content/uploads/2017/07/What-Is-A-Man-Bun-Top-Knot-Hairstyle-Graphic.png"
        }
    ]
)

heart_face = Face(
    hairstyle = [
        {"name":"Clean shaven head",
        "image_url":"https://2x1dks3q6aoj44bz1r1tr92f-wpengine.netdna-ssl.com/wp-content/uploads/2017/07/What-Is-A-Mens-Shaved-Head-Style.png"
        },
        {
            "name":"Buzz cut hairstyle",
            "image_url":"https://2x1dks3q6aoj44bz1r1tr92f-wpengine.netdna-ssl.com/wp-content/uploads/2017/07/What-Is-A-Buzz-Cut-Hairstyle-Graphic.png"
        },
        {
            "name":"Comb over hair style",
            "image_url":"https://2x1dks3q6aoj44bz1r1tr92f-wpengine.netdna-ssl.com/wp-content/uploads/2017/07/What-Is-A-Comb-Over-Hairstyle-Graphic.png"
        },
        {
            "name":"Fringe hair style",
            "image_url":"https://2x1dks3q6aoj44bz1r1tr92f-wpengine.netdna-ssl.com/wp-content/uploads/2017/07/What-Is-A-Fringe-Hairstyle-Graphic.png"
        },
        {
            "name":"Man bun hairstyle",
            "image_url":"https://2x1dks3q6aoj44bz1r1tr92f-wpengine.netdna-ssl.com/wp-content/uploads/2017/07/What-Is-A-Man-Bun-Top-Knot-Hairstyle-Graphic.png"
        }
    ]
)
ohlong_face = Face(
    hairstyle=[
        {"name":"Clean shaven head",
        "image_url":"https://2x1dks3q6aoj44bz1r1tr92f-wpengine.netdna-ssl.com/wp-content/uploads/2017/07/What-Is-A-Mens-Shaved-Head-Style.png"
        },
        {
            "name":"Buzz cut hairstyle",
            "image_url":"https://2x1dks3q6aoj44bz1r1tr92f-wpengine.netdna-ssl.com/wp-content/uploads/2017/07/What-Is-A-Buzz-Cut-Hairstyle-Graphic.png"
        },
        {
            "name":"Comb over hair style",
            "image_url":"https://2x1dks3q6aoj44bz1r1tr92f-wpengine.netdna-ssl.com/wp-content/uploads/2017/07/What-Is-A-Comb-Over-Hairstyle-Graphic.png"
        },
        {
            "name":"Fringe hair style",
            "image_url":"https://2x1dks3q6aoj44bz1r1tr92f-wpengine.netdna-ssl.com/wp-content/uploads/2017/07/What-Is-A-Fringe-Hairstyle-Graphic.png"
        },
        {
            "name":"Man bun hairstyle",
            "image_url":"https://2x1dks3q6aoj44bz1r1tr92f-wpengine.netdna-ssl.com/wp-content/uploads/2017/07/What-Is-A-Man-Bun-Top-Knot-Hairstyle-Graphic.png"
        }
    ]
)
round_face = Face(
    hairstyle = [
        {"name":"Clean shaven head",
        "image_url":"https://2x1dks3q6aoj44bz1r1tr92f-wpengine.netdna-ssl.com/wp-content/uploads/2017/07/What-Is-A-Mens-Shaved-Head-Style.png"
        },
        {
            "name":"Buzz cut hairstyle",
            "image_url":"https://2x1dks3q6aoj44bz1r1tr92f-wpengine.netdna-ssl.com/wp-content/uploads/2017/07/What-Is-A-Buzz-Cut-Hairstyle-Graphic.png"
        },
        {
            "name":"Comb over hair style",
            "image_url":"https://2x1dks3q6aoj44bz1r1tr92f-wpengine.netdna-ssl.com/wp-content/uploads/2017/07/What-Is-A-Comb-Over-Hairstyle-Graphic.png"
        },
        {
            "name":"Fringe hair style",
            "image_url":"https://2x1dks3q6aoj44bz1r1tr92f-wpengine.netdna-ssl.com/wp-content/uploads/2017/07/What-Is-A-Fringe-Hairstyle-Graphic.png"
        },
        {
            "name":"Man bun hairstyle",
            "image_url":"https://2x1dks3q6aoj44bz1r1tr92f-wpengine.netdna-ssl.com/wp-content/uploads/2017/07/What-Is-A-Man-Bun-Top-Knot-Hairstyle-Graphic.png"
        }
    ]
)
oval_face = Face(
    hairstyle = [
        {"name":"Clean shaven head",
        "image_url":"https://2x1dks3q6aoj44bz1r1tr92f-wpengine.netdna-ssl.com/wp-content/uploads/2017/07/What-Is-A-Mens-Shaved-Head-Style.png"
        },
        {
            "name":"Buzz cut hairstyle",
            "image_url":"https://2x1dks3q6aoj44bz1r1tr92f-wpengine.netdna-ssl.com/wp-content/uploads/2017/07/What-Is-A-Buzz-Cut-Hairstyle-Graphic.png"
        },
        {
            "name":"Comb over hair style",
            "image_url":"https://2x1dks3q6aoj44bz1r1tr92f-wpengine.netdna-ssl.com/wp-content/uploads/2017/07/What-Is-A-Comb-Over-Hairstyle-Graphic.png"
        },
        {
            "name":"Fringe hair style",
            "image_url":"https://2x1dks3q6aoj44bz1r1tr92f-wpengine.netdna-ssl.com/wp-content/uploads/2017/07/What-Is-A-Fringe-Hairstyle-Graphic.png"
        },
        {
            "name":"Man bun hairstyle",
            "image_url":"https://2x1dks3q6aoj44bz1r1tr92f-wpengine.netdna-ssl.com/wp-content/uploads/2017/07/What-Is-A-Man-Bun-Top-Knot-Hairstyle-Graphic.png"
        }
    ]
)
square_face = Face(
    hairstyle = [
        {"name":"Clean shaven head",
        "image_url":"https://2x1dks3q6aoj44bz1r1tr92f-wpengine.netdna-ssl.com/wp-content/uploads/2017/07/What-Is-A-Mens-Shaved-Head-Style.png"
        },
        {
            "name":"Buzz cut hairstyle",
            "image_url":"https://2x1dks3q6aoj44bz1r1tr92f-wpengine.netdna-ssl.com/wp-content/uploads/2017/07/What-Is-A-Buzz-Cut-Hairstyle-Graphic.png"
        },
        {
            "name":"Comb over hair style",
            "image_url":"https://2x1dks3q6aoj44bz1r1tr92f-wpengine.netdna-ssl.com/wp-content/uploads/2017/07/What-Is-A-Comb-Over-Hairstyle-Graphic.png"
        },
        {
            "name":"Fringe hair style",
            "image_url":"https://2x1dks3q6aoj44bz1r1tr92f-wpengine.netdna-ssl.com/wp-content/uploads/2017/07/What-Is-A-Fringe-Hairstyle-Graphic.png"
        },
        {
            "name":"Man bun hairstyle",
            "image_url":"https://2x1dks3q6aoj44bz1r1tr92f-wpengine.netdna-ssl.com/wp-content/uploads/2017/07/What-Is-A-Man-Bun-Top-Knot-Hairstyle-Graphic.png"
        }
    ]
)
triangle_face = Face(
    hairstyle = [
        {"name":"Clean shaven head",
        "image_url":"https://2x1dks3q6aoj44bz1r1tr92f-wpengine.netdna-ssl.com/wp-content/uploads/2017/07/What-Is-A-Mens-Shaved-Head-Style.png"
        },
        {
            "name":"Buzz cut hairstyle",
            "image_url":"https://2x1dks3q6aoj44bz1r1tr92f-wpengine.netdna-ssl.com/wp-content/uploads/2017/07/What-Is-A-Buzz-Cut-Hairstyle-Graphic.png"
        },
        {
            "name":"Comb over hair style",
            "image_url":"https://2x1dks3q6aoj44bz1r1tr92f-wpengine.netdna-ssl.com/wp-content/uploads/2017/07/What-Is-A-Comb-Over-Hairstyle-Graphic.png"
        },
        {
            "name":"Fringe hair style",
            "image_url":"https://2x1dks3q6aoj44bz1r1tr92f-wpengine.netdna-ssl.com/wp-content/uploads/2017/07/What-Is-A-Fringe-Hairstyle-Graphic.png"
        },
        {
            "name":"Man bun hairstyle",
            "image_url":"https://2x1dks3q6aoj44bz1r1tr92f-wpengine.netdna-ssl.com/wp-content/uploads/2017/07/What-Is-A-Man-Bun-Top-Knot-Hairstyle-Graphic.png"
        }
    ]
)
diamond_face.save()
heart_face.save()
ohlong_face.save()
round_face.save()
oval_face.save()
square_face.save()
triangle_face.save()
