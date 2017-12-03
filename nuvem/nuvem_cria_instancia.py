import shade



# CONECTANDO NA NUVEM
nuvem = shade.openstack_cloud(cloud='envvars')



# INSERINDO CHAVE DE ACESSO
print('\nInserindo CHAVE de acesso')
#chave_nome_par = "time11famaral"
chave_nome_par = "time11small"
diretorio = '/home/famaral/codesMint/openstack-time-11/nuvem/.chave/'
chave_publica = open(diretorio+chave_nome_par+'.pem','r').read().strip()
if nuvem .search_keypairs(chave_nome_par):
    print('Chave ja existente e sera usada')
else:
    print('Adicionando chave')
    nuvem.create_keypair(chave_nome_par,chave_publica)
for chave in nuvem.list_keypairs():
    print(chave.name, chave.public_key[:60]+'...')



# CRIANDO GRUPO
print('\nCriando GRUPO de acesso e abrindo PORTAS')
grupo_nome = 'grupo11'
portas = [80,22,40000]
if nuvem.search_security_groups(grupo_nome):
    print('Grupo ja existente e sera usado')
else:
    print('Adicionando grupo')
    nuvem.create_security_group(grupo_nome,'Grupo de acesso vriado')
    for porta in portas:
        nuvem.create_security_group_rule(grupo_nome,porta,porta,'TCP')
    print('Portas', portas, 'abertas')
print(grupo_nome, nuvem.get_security_group(grupo_nome).name)



# REDE E SUB REDE
print("\nCriando rede")
nome_da_rede = 'time11-rede'
if not nuvem.search_networks(nome_da_rede):
    nuvem.create_network(nome_da_rede)
print("Rede " + nome_da_rede + " criada")

nome_subrede = 'time11-subrede'
if not nuvem.search_subnets(nome_subrede):
    nuvem.create_subnet(nome_da_rede,
                        subnet_name=nome_subrede,
                        enable_dhcp=True,
                        cidr='192.168.0.0/24',
                        gateway_ip='192.168.0.1',
                        dns_nameservers=['8.8.8.8'])
print("SubRede " + nome_subrede + " criada")



# ROTEADOR
print("\nCriando roteador")
roteador = 'time11-roteador'
id_public = nuvem.get_network('public_network').id
if not nuvem.search_routers(roteador):
    nuvem.create_router(name=roteador,
                        enable_snat=True,
                        ext_gateway_net_id=id_public)
print("Roteador " + roteador + " criado!")

print("\nIterface do roteador")
roteador_dicionario = nuvem.get_router(roteador)
id_subrede = nuvem.get_subnet(nome_subrede).id
if not nuvem.list_router_interfaces(roteador_dicionario):
    nuvem.add_router_interface(roteador_dicionario, subnet_id=id_subrede)
print("Interface criada para o roteador " + roteador)



# INSTANCIA
print("\Criando instancia")
nome_imagem = 'Ubuntu 16.04 LTS Xenial'
sabor = 'm1.small'
nome_instancia = 'time11_Vaga_Azul_42'
#endereco_ip = dict(nuvem.list_floating_ips()[0])['floating_ip_address']
ex_userdata = open('./sobe_servidor.sh', 'r').read()
print(ex_userdata)

if not nuvem.get_server(nome_instancia):
    nuvem.create_server(nome_instancia,
                        image=nome_imagem,
                        flavor=sabor,
                        wait=True,
                        auto_ip=True,
                        #ips=[endereco_ip],
                        key_name=chave_nome_par,
                        security_groups=[grupo_nome],
                        network=nome_da_rede,
                        userdata=ex_userdata)
