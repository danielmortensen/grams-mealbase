input_params = {'valid' : {
                    'people': [{'name'         : 'john doe',
                                'billing unit' : 'doe family'},
                               {'name'        : 'jane joe',
                                'billing unit' : 'doe family'}],
                    'users' : [{'name' : 'john doe', 
                                'billing unit' : 'doe family'
                               },
                               {'name'         : 'jane joe',
                                'billing unit' : 'doe family'
                               }],
                    'royals' : [{'name' : 'john doe'}],
                    'food admins' : [{'name' : 'jane joe'}],
                    'billing unit' : [{'name' : 'doe family'}],
                    'logins': [{'name' : 'john doe',
                                'email' : 'doe.john@testnet.com',
                                'password' : 'john_password'},
                                {'name' : 'jane joe',
                                 'email' : 'doe.jane@testnet.com',
                                 'password' : 'jane_password'}]
},
               'invalid' : {
                   'people': [{'name' : 'kevin doe',
                               'billing unit' : 'the no-goods'},
                              {'name' : 'max doe',
                               'billing unit' : 'the no-goods'}],
                    'users' : [{'name' : 'kevin doe',
                                'billing unit' : 'the no-goods'},
                               {'name' : 'max doe',
                                'billing unit' : 'the no-goods'}],
                    'royals' : [{'name' : 'kevin doe'},
                                {'name' : 'max doe'}],
                    'food admins': [{'name' : 'kevin doe'},
                                    {'name' : 'max doe'}],
                    'billing unit' : [{'name' : 'the no-goods'}],
                    'logins' : [{'name' : 'kevin doe',
                                 'email' : 'doe.kevin@testnet.com'},
                                {'name' : 'max doe',
                                 'email' : 'doe.max@testnet.com'}]
               }
}