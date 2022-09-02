class GameObject:
    def __init__(self, name: str, the_name: str = None):
        self.name = name
        self.description_string = ""
        self.inline_description_string = None
        self.described = False
        self.objects = []

        self.the_name = the_name if the_name else name.lower()

        self.flags = {
            'DESC_IN_PARENT_DESC': True,
            'INLINE_DESC_IN_PARENT_DESC': True
        }

        self.parent = None

    def add_object(self, g_object):
        g_object.parent = self
        self.objects.append(g_object)

    def is_of_type(self, extendable):
        if hasattr(self, extendable.__name__.lower()):
            return True
        return False

    def description(self):
        pass

    def final_description(self):
        self.described = True
        desc = self.description()

        if desc is None:
            return ""

        for sub_g_object in self.objects:
            sub_g_object_desc = sub_g_object.final_inline_description() if sub_g_object.flags[
                'INLINE_DESC_IN_PARENT_DESC'] else ""

            desc += f"\n{sub_g_object_desc}" if sub_g_object_desc else ""

        return desc

    def get_all_subobjects(self):
        all_objects = []

        for object in self.objects:
            all_objects.append(object)

            if object.get_all_subobjects():
                all_objects.extend(object.get_all_subobjects())

        return all_objects

    def inline_description(self):
        return self.inline_description_string

    def final_inline_description(self):
        desc = self.inline_description()

        for sub_g_object in self.objects:
            sub_g_object_desc = sub_g_object.final_inline_description()

            desc += f"\n{sub_g_object_desc}" if sub_g_object_desc else ""

        return desc
