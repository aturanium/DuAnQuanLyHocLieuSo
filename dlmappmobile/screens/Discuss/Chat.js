import { ActivityIndicator, FlatList, Image, Text, TouchableOpacity, View } from "react-native";
import { List, Searchbar } from "react-native-paper";
import MyStyles from "../../styles/MyStyles";
import { useEffect, useState } from "react";
import Apis, { endpoints } from "../../utils/Apis";

const Chat = () => {
    const [chat, setChat] = useState([]);
    const [loading, setLoading] = useState(false);
    const [q, setQ] = useState("");

    const loadChat = async() =>{
        try {
            setLoading(true)
        
            const res = await Apis.get(endpoints["users"], {
                params: q ? { q } : {}
            });
            setChat(res.data)
            
            } catch (ex) {
                console.error(ex);
            } finally {
                 setLoading(false);
            }
    }

    useEffect(() => {
            let timer = setTimeout(() => {
                    loadChat();
            }, 500);
            return () => clearTimeout(timer);
        }, [q]);


     return(
        <>
        <Searchbar placeholder="Tìm kiếm" style={[MyStyles.margin]} value={q} onChangeText={setQ}/>
        <FlatList data={chat} ListFooterComponent={loading && <ActivityIndicator size="large" />} renderItem={({ item }) => <List.Item
                                                        title={item.last_name +" "+ item.first_name}
                                                        left={() => <TouchableOpacity onPress={() => {} } >
                                                            <Image source={item.avatar ? { uri: item.avatar } : require('../../assets/images/memecat2.jpg')} style={MyStyles.image} />
                                                        </TouchableOpacity>} />
                    } />
        </>
    );
}

export default Chat;