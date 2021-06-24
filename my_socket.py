# from os import close
# import socket

# def main():
#     server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#     server_socket.bind(('localhost', 5000))
#     server_socket.listen()
    
#     while True:
#         client_socket, addr = server_socket.accept()
#         request = client_socket.recv(1024)
#         print('request: ', request)
#         print('-'*50)
#         print('addr: ', addr)
#         print('='*50)
#         client_socket.sendall(('hello world'.encode()))
#         client_socket.close()

# if __name__ == '__main__':
#     main()


    # @staticmethod
    # def _regroup_tariffs(tariffs_filter: Dict[str, Any], tariffs: Tuple[Tariff]) -> List:
    #     """Function for sorting and regrouping tariffs list.

    #     Args:
    #         tariffs_filter: Dictionary with optional Sort parameters after schema validation
    #         tariffs: List of tariffs

    #     Returns:
    #         Regrouped tariffs list by utilities and sorted by filter params

    #     """
    #     sort = tariffs_filter.pop('sort', 'name')
    #     order = tariffs_filter.pop('order', 'asc')
    #     order_switch = {'asc': False, 'desc': True}
    #     sort_switch = {
    #         'id': (lambda t: t.id),
    #         'name': (lambda t: t.name),
    #     }
    #     group_tariffs = []
    #     uniq_utilities = []

    #     for key, group_items in groupby(tariffs, key=lambda t: t.utility):
    #         group_tariffs.append(list(group_items))
    #         uniq_utilities.append(key)

    #     for i, key in enumerate(uniq_utilities):
    #         group_tariffs[i] = sorted(group_tariffs[i], key=sort_switch[sort], reverse=order_switch[order])
    #         key.tariffs = group_tariffs[i]

    #     return uniq_utilities