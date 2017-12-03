import shade

# CONECTANDO NA NUVEM
nuvem = shade.openstack_cloud(cloud='envvars')

# LISTANDO IMAGENS
print('\nIMAGENS existentes no OpenStack\n')
for imagem in nuvem.list_images():
    print("{:<30} id: {:<30}".format(imagem.name, imagem.id))

# LISTANDO SABORES
print('\nSABORES (flavors) existentes\n')
for sabor in nuvem.list_flavors():
    print("{:<20} {:<2} vcpus {:<6} MB {:<4} Disk - {}".format(
        sabor.name, sabor.vcpus, sabor.ram, sabor.disk, sabor.id))
