import requests
import json
import random



origonal_anime_list = ['bleach', 'black_clover', 'dragon_ball', 'jujutsu_kaisen', 'fma_brotherhood', 'naruto',
                       'gintama', 'one_piece', 'demon_slayer', 'attack_on_titan', 'hunter_x_hunter',
                       'boku_no_hero_academia']

anime_dict1 = {1: 'bleach', 2: 'black_clover', 3: 'dragon_ball', 4: 'jujutsu_kaisen', 5: 'fma_brotherhood',
              6: 'naruto', 7: 'gintama', 8: 'one_piece', 9: 'demon_slayer', 10: 'attack_on_titan', 11: 'hunter_x_hunter',
              12: 'boku_no_hero_academia'}


anime_length_dict = {}
if __name__=='__main__':
    user_input = ''
    score = 0  # set score equal to zero
    while user_input != 'stop':
        animes_num_picked = []
        anime_fact_print_order_dict = {}
        anime_dict = anime_dict1
        copied_anime_list = origonal_anime_list
        new_anime_list = []

        for i in range(0, 4):  # for range loop to iterate 4 times with max index of 3
            anime_picked = random.randint(0, ((len(copied_anime_list)) -1))  # randomly pick the key for the anime to have a fact about it displayed
            anime_picked = anime_picked - 1
            animes_num_picked.append(anime_picked)  #line to add the number of the anime picked to the animes_num_picked list


            random_picked_anime = copied_anime_list[anime_picked]  # random_picked_anime is assigned with the anime --
            # that got picked at the index value of the random number from the copied_anime_list

            anime_fact_print_order_dict[(i+ 1)] = random_picked_anime  #add a new dictionary key and value with the key --
            # being the line number that the fact was printed on and the value of that line number key
            # being the name of the anime that the fact on that line is about



            response = requests.get(f'https://anime-facts-rest-api.herokuapp.com/api/v1/{random_picked_anime}')  # assign --
            # response with the requested list of facts for the randomly picked anime

            total_facts = response.json()['total_facts']


            random_quote_num = random.randint(1, total_facts - 1)


            correct_anime_list_index_num = random.randint(1, (len(animes_num_picked)))  ##
        ## Lines (43- 46) to figure out what--
            correct_anime_ = anime_fact_print_order_dict[correct_anime_list_index_num]  ## the correct anime will be



            # set response equal to the facts about the randomly picked anime
            quote = response.json()['data'][random_quote_num]['fact']  # set the quote equal to the data
            print('\n', quote)

            del copied_anime_list[anime_picked]


        correct_anime = ''

        if correct_anime_ == 'fma_brotherhood':
            correct_anime = 'Fullmetal Alchemist Brotherhood'
        elif '_' in correct_anime_:  ## if statement to make the correct_anime variable with spaces instead of underscores
           correct_anime_list = correct_anime_.split('_')
           for index in range(len(correct_anime_list)):  #for statement to capitalize the first letter of the anime names
               if index == ((len(correct_anime_list)) - 1):

                   correct_anime += correct_anime_list[index].capitalize()
               else:
                   correct_anime += f'{correct_anime_list[index].capitalize()} '
        else:
            correct_anime += correct_anime_.capitalize()  #if anime is only one word long then it capitalizes that first letter



        user_input = int(input(f'\n which one of these facts of these facts was from {correct_anime}? '))


        line_guess = user_input




        if anime_fact_print_order_dict[line_guess] == correct_anime:
            score = score + 1
            print(f'Correct! your score now is {score} :)\n')
        else:
            print(f'Incorrect :( your score is still {score}\n')

        user_input = input('Enter any key to play again, enter stop to quit \n')
    print('\nGoodbye! Your final score was', score)
