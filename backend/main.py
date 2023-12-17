from flask import Flask, jsonify, request
from flask_cors import CORS


app = Flask(__name__)
CORS(app)

items = []


@app.route("/")
def main():
    return "Hello, World"


@app.route("/api/items", methods=["GET"])
def get_all_items():
    return jsonify(items)


@app.route("/api/upload-image", methods=["POST"])
def upload_image():
    data = request.json
    title = data.get("title", "")
    description = data.get("description", "")
    base64_image = data.get("image", "")
    id = len(items) + 1

    items.append(
        {"id": id, "title": title, "description": description, "image": base64_image}
    )

    return jsonify({"message": "Data uploaded successfully"})


@app.route("/api/delete-image/<int:image_id>", methods=["DELETE"])
def delete_image(image_id):
    # Find the index of the image with the specified ID
    index_to_delete = None
    for i, item in enumerate(items):
        if item["id"] == image_id:
            index_to_delete = i
            break

    # If the image ID is found, delete it
    if index_to_delete is not None:
        deleted_item = items.pop(index_to_delete)
        return jsonify(
            {
                "message": f"Image with ID {image_id} deleted successfully",
                "deleted_item": deleted_item,
            }
        )
    else:
        return jsonify({"error": f"Image with ID {image_id} not found"}), 404


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
