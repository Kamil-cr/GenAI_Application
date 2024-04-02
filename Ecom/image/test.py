@app.post("/image", response_model=Image)
async def create_image(image: UploadFile, session: Annotated[Session, Depends(db_session)]):
    image = await image.read()
    image_data = Image(data=image)
    session.add(image_data)
    session.commit()
    session.refresh(image_data)
    return {"Response": "Successfull"}

@app.get("/image/{id}", response_model=Image)
def get_image(id: int, session: Annotated[Session, Depends(db_session)]):
    image_model = session.exec(select(Image).filter(Image.id == id)).first()
    binary_data = image_model.data
    image = PILImage.open(io.BytesIO(binary_data))

    # Convert the image to base64 encoding
    buffered = io.BytesIO()
    image.save(buffered, format="PNG")
    img_str = base64.b64encode(buffered.getvalue()).decode()

    # Render the image in HTML
    html_content = f'<img src="data:image/jpeg;base64,{img_str}">'

    return HTMLResponse(content=html_content, status_code=200)