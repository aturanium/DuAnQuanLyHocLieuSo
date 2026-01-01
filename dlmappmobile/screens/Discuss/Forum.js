import { useEffect, useState } from "react";
import { ActivityIndicator, FlatList, ScrollView, Text, TouchableOpacity, View } from "react-native";
import Apis, { endpoints } from "../../utils/Apis";
import { Card, List, Searchbar } from "react-native-paper";
import MyStyles from "../../styles/MyStyles";


const Forum = () => {
    const [questions, setQuestions] = useState([]);
    const [loading, setLoading] = useState(false);
    const [q, setQ] = useState("");
    const [page, setPage] = useState(1);


    const loadQuestions = async () => {
        try {
            setLoading(true)

            let url = `${endpoints['questions']}`;


            console.info(url);

            let res = await Apis.get(url);
            setQuestions(res.data)


        } catch (ex) {
            console.error(ex);
        } finally {
            setLoading(false);
        }
    }


    useEffect(() => {
        let timer = setTimeout(() => {
            if (page > 0)
                loadQuestions();
        }, 500);

        return () => clearTimeout(timer);
    }, [q, page]);

    useEffect(() => {
        setPage(1);
    }, [q])

    const loadMore = () => {
        if (page > 0 && !loading)
            setPage(page + 1);
    }

    return (
        <>
            <Searchbar placeholder="Tim kiếm .... " style={[MyStyles.margin, MyStyles.marginBottom]} />
            <FlatList ListFooterComponent={loading && <ActivityIndicator size="large" />} data={questions} onEndReached={loadMore}
                renderItem={({ item }) => (
                    <TouchableOpacity onPress={() => {}}>
                        <Card style={[MyStyles.margin]}>
                            <Card.Title
                                title={item.created_by.first_name}
                                subtitle={item.title}
                            />
                            <Card.Content>
                                <Text numberOfLines={2}>{item.content}</Text>
                            </Card.Content>
                            <Card.Actions>
                                <Text>Trả lời: {item.answer_count}</Text>
                            </Card.Actions>
                        </Card>
                    </TouchableOpacity>
                )} />
        </>
    );
}

export default Forum;