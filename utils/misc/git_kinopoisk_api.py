import json

from kinopoisk_dev import KinopoiskDev, Field, MovieParams

from config_data.config import KINOPOISK_DEV_TOKEN
from database.core import inter_db, db, History


def kinopisk_api(yars: str, rat_kp: str, sort=1) -> list:  # sort = 1 or -1
    create = inter_db.create()
    create(db, History, [{"yars": yars, 'rat_kp': rat_kp, 'sort': sort}])
    kp = KinopoiskDev(token=KINOPOISK_DEV_TOKEN)
    items = kp.movies([
        MovieParams(field=Field.YEAR, search=str(yars)),
        MovieParams(field='rating.kp', search=str(rat_kp)),
        MovieParams(sortField="rating.kp", sortType=sort),
    ], limit=5, page=1)
    print('respaunt', items)
    data = json.loads(items.json())
    print('respaunt2', data)
    result = []

    if data['docs'][0]['name'] is not None:
        for i_docs in data['docs']:
            result.append({"poster": i_docs["poster"]["previewUrl"], 'name': i_docs['name'], 'year': i_docs['year'],
                           "rating": i_docs["rating"]["kp"]})

    return result


if __name__=="__main__":
    kinopisk_api()

