from marshmallow import Schema, fields

class PlainItemSchema(Schema):
    id = fields.Int(dump_only=True)
    name = fields.Str(required=True)
    price = fields.Float(required=True)

class PlainStoreSchema(Schema):
    id = fields.Int(dump_only=True)
    name = fields.Str()

class PlainTagSchema(Schema):
    id = fields.Int(dump_only=True)
    name =fields.Str()

class ItemSchema(Schema):
    store_id = fields.Int(required=True, load_only=True)
    store = fields.Nested(PlainStoreSchema(), dump_only=True)
    tags = fields.List(fields.Nested(PlainTagSchema(), dump_only=True))


class StoreSchema(PlainStoreSchema):
    items = fields.List(fields.Nested(PlainItemSchema()), dump_only=True)
    tags = fields.List(fields.Nested(PlainTagSchema()), dump_only=True)

class TagSchema(Schema):
    store_id = fields.Int(required=True, load_only=True)
    store = fields.Nested(PlainStoreSchema(), dump_only=True)
    items = fields.Nested(PlainItemSchema(), dump_only=True)

class ItemUpdateSchema(Schema):
    price = fields.Float()
    name = fields.Str()
    
class TagAndItemShcema(Schema):
    tag = fields.Nested(TagSchema)
    item = fields.Nested(ItemSchema)
    message = fields.Str()


class UserSchema(Schema):
    id = fields.Int(dump_only=True)
    username = fields.Str(required=True)
    password = fields.Str(required=True, load_only=True)