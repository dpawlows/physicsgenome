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


def save_course(object,u_object,i_name,*args,**kwargs):
    '''Need to supply the associated university in order to make sure we have a unique
    is unique

    '''

    if kwargs.has_key('description'):
        description = kwargs['description']
    else:
        description = i_name

    # newid = chopr('000'+str(u_object.pk),3)
    name = i_name.replace(' ','_')
    # code = newid+'_'+name
    code = name

    try:
        return object.objects.get(code=code)
    except:
        new_object = object(code=code)
        # new_object.name = i_name
       
        if hasattr(new_object, 'description'):
            new_object.description=description
        
        for attribute in kwargs:
            attribute = setattr(new_object, attribute, kwargs[attribute]) 

        new_object.university = u_object
        new_object.save()


        return new_object