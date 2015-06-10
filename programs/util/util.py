def save_code(object, i_code, *args, **kwargs):
    if kwargs.has_key('description'):
        description = kwargs['description']
    else:
        description = i_code
        
    code = i_code.replace(' ','_')
        
    try:
        return object.objects.get(code=code)
    except:
        new_object = object(code=code)
        if hasattr(new_object, 'description'):
            new_object.description=description
        for attribute in kwargs:
            attribute = setattr(new_object, attribute, kwargs[attribute]) 
            
        new_object.save()
        return new_object