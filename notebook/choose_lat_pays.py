# Ici je ne prend que les pays qui ont plus de 10 filières (sinon c est ilisible sur une carte)
def choose_lat_pays(pays, latitudeCVS):

    lat_pays=dico_plage_latitude.get(pays)
    if lat_pays:
        latitude = random.uniform(lat_pays['max'], lat_pays['min'])
    else:
        latitude = latitudeCVS + random.uniform(-0.5, 0.5)  # valeur de base pour tous les "petits" pays

    return latitude

if __name__ == '__main__':
    print("calling la fonction : choose_lat_pays")
    main()