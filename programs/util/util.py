import pdb

def chopr(sval,n):
    if len(sval) < n: n = len(sval)
    return sval[len(sval)-n:len(sval)]


def save_code(object, i_code, *args, **kwargs):
    # pdb.set_trace()

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


def save_course(object,i_name,i_university_pk,*args,**kwargs):

    if kwargs.has_key('description'):
        description = kwargs['description']
    else:
        description = i_name

    id = chopr('00'+str(i_university_pk),3)

    name = i_name.replace(' ','_')
    code = id+'_'+name

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