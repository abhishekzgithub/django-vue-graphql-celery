from . import models
import csv
import traceback
def load_to_db():
    try:
        latest_entry=models.Document.objects.latest('id')
        doc=latest_entry.document.path
        # doc_path.multiple_chunks
        with open(doc, mode='r') as f:
            reader = csv.reader(f)
            for row in reader:
                p= models.Products(
                    name=row[0],
                    sku=row[1],
                    description=row[2],
                    flag='inactive'
                    )
                p.save()
    except :
        print(traceback.format_exc)
    finally:
        print("loaded to db")