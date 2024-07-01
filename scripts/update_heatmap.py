import os
from utils import upload_image
from notion_helper import NotionHelper


def get_file(dir):
    dir =f"./{dir}"
    if os.path.exists(dir) and os.path.isdir(dir):
        entries = os.listdir(dir)
        file_name = entries[0] if entries else None
        return file_name
    else:
        print("OUT_FOLDER does not exist.")
        return None


def update_heatmap(dir, block_id):
    image_file = get_file(dir)
    if image_file:
        image_url = f"https://raw.githubusercontent.com/{os.getenv('REPOSITORY')}/{os.getenv('REF').split('/')[-1]}/{dir}/{image_file}"
        heatmap_url = f"https://heatmap.malinkang.com/?image={image_url}"
        if block_id:
            notion_helper.update_heatmap(block_id=block_id, url=heatmap_url)


if __name__ == "__main__":
    notion_helper = NotionHelper()
    update_heatmap("heatmap/todo",notion_helper.todo_heatmap_block_id)
    update_heatmap("heatmap/tomato",notion_helper.tomato_heatmap_block_id)
