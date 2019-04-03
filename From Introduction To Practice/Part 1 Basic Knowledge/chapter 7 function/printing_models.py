unprinted_designs = ['iphone case', 'robot pendant', 'dodecahedron']
completed_models = []

# while unprinted_designs:
#     current_design = unprinted_designs.pop()
#
#     print('Printing model: ' + current_design)
#     completed_models.append(current_design)
#
# print('The following models have been printed:'.center(50, '*'))
# for completed_model in completed_models:
#     print(completed_model)


def print_models(unprinted_designs, completed_models):
    while unprinted_designs:
        current_design = unprinted_designs.pop()

        print('Printing model: ' + current_design)
        completed_models.append(current_design)


def show_completed_models(completed_models):
    print('The following models have been printed:'.center(50, '*'))
    for completed_model in completed_models:
        print(completed_model)


print_models(unprinted_designs, completed_models)
show_completed_models(completed_models)
